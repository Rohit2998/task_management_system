# Task Management API

## Overview
This project provides a simple task management API using Django and Django REST Framework. It allows users to create, update, delete, and assign tasks while implementing authentication, rate-limiting, and AWS Lambda integration.

## Requirements
- Python with Django and Django REST Framework
- PostgreSQL (Dockerized)
- Redis (Dockerized for caching and rate-limiting)
- AWS Lambda integration for task notifications

## Features
- **CRUD operations** for task management
- **User authentication** using Django’s built-in auth system
- **Token-based authentication** for API access
- **Task filtering** by status (pending/completed)
- **Rate-limited API endpoints** using Django’s throttling and caching
- **AWS Lambda integration** to send notifications on task completion

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Rohit2998/task_management_system.git
cd task_management_system
```

### 2. Run the Application using Docker
```sh
docker-compose up --build
```

### 3. Migrate the Database
```sh
docker-compose exec web python manage.py migrate
```

### 4. Create a Superuser (Optional)
```sh
docker-compose exec web python manage.py createsuperuser
```

## API Endpoints
### User Authentication
- **Register User:** `POST http://127.0.0.1:8000/register/`
- **Get Token:** `POST http://127.0.0.1:8000/api/token/`

### Task Management
- **List Tasks:** `GET /tasks/`
- **Retrieve Task:** `GET /tasks/{id}/`
- **Create Task:** `POST /tasks/`
- **Update Task:** `PUT /tasks/{id}/`
- **Delete Task:** `DELETE /tasks/{id}/`

## AWS Lambda Integration
- When a task is marked as completed, an AWS Lambda function is triggered to log a notification.

## Design Considerations
- **Dockerized setup** ensures consistency across environments.
- **Rate-limiting and caching** optimize performance.
- **AWS Lambda integration** showcases scalability and cloud event handling.



