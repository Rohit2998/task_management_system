from rest_framework import viewsets, permissions, throttling, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from .utils import trigger_lambda  # Util


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing tasks with CRUD operations and caching.
    Supports filtering by status and rate-limiting.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [throttling.UserRateThrottle]

    def get_queryset(self):
        """Retrieve all tasks, optionally filtered by status."""
        self.queryset = Task.objects.all()
        status = self.request.query_params.get("status", None)
        if status:
            return self.queryset.filter(status=status)
        return self.queryset

    def list(self, request, *args, **kwargs):
        """Return cached task list if available, otherwise fetch from DB."""
        cache_key = "tasks_list"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, timeout=60)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """Return a single task, using cache if available."""
        task_id = kwargs.get("pk")
        cache_key = f"task_{task_id}"
        task_data = cache.get(cache_key)

        if not task_data:
            # Fetch from DB if not cached
            instance = get_object_or_404(Task, pk=task_id)
            serializer = self.get_serializer(instance)
            task_data = serializer.data
            cache.set(cache_key, task_data, timeout=300)

        return Response(task_data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        """Create a new task and clear the cached task list."""
        cache.delete("tasks_list")
        serializer.save()

    def perform_update(self, serializer):
        """Update a task, clear cache, and trigger Lambda if completed."""
        cache.delete("tasks_list")
        instance = serializer.save()
        if instance.status == "completed":
            print("triggered")
            trigger_lambda(instance)

    def perform_destroy(self, instance):
        """Clear cache when a task is deleted"""
        cache.delete("tasks_list")
        instance.delete()
