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
### POSTMAN COLLECTION
- import the Postman collection from the `postman_collection.json` file in the root directory to ease the testing of API endpoints.
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


## AWS Lambda Notification Logs

We use an AWS Lambda function to log notifications when a task is marked as completed. The `lambda_function.py` contains the following logic:

UPDATE in Settings :

- AWS_REGION = "your region" #"us-east-1"
- AWS_LAMBDA_NAME = "lambda function name"# "test_func"


### -Note : Please add you aws creds in docker compose for successful integeration


```python
import json

def lambda_handler(event, context):
    task_title = event.get("task_title", "Unknown Task")
    assigned_to = event.get("assigned_to", "Unassigned")
    
    message = f"Task '{task_title}' assigned to {assigned_to} is now completed."
    
    print(f"Lambda Notification: {message}")

    return {"statusCode": 200, "body": json.dumps({"message": message})}
```

### How the Lambda Logs Work:
1. When a task is updated to "completed," the `perform_update` method in `TaskViewSet` triggers the Lambda function.
2. The Lambda function receives the task details and logs a message.
3. You can view the logs in the AWS Lambda console under **Monitoring → CloudWatch 
4. On successfull integeration you recieve see logs in lambda like below

2025-03-19T20:46:57.954Z
INIT_START Runtime Version: python:3.13.v13 Runtime Version ARN: arn:aws:lambda:us-east-1::runtime:b881cbc9a10a8bcb3def9d9e9fe38f922bb36510a1d92d4ce85cf2a899eeabd8

2025-03-19T20:46:58.069Z
START RequestId: 5b729abf-d773-4285-ae41-c7a0a69fa0a3 Version: $LATEST
2025-03-19T20:46:58.070Z

### Lambda Notification: Task 'Task is Still Pending' assigned to test1 is now completed.

2025-03-19T20:46:58.072Z
END RequestId: 5b729abf-d773-4285-ae41-c7a0a69fa0a3
2025-03-19T20:46:58.083Z
REPORT RequestId: 5b729abf-d773-4285-ae41-c7a0a69fa0a3 Duration: 2.04 ms Billed Duration: 3 ms Memory Size: 128 MB Max Memory Used: 30 MB Init Duration: 112.03 ms
No newer events at this moment. 
Auto retry paused.
 

## Design Considerations
- **Dockerized setup** ensures consistency across environments.
- **Rate-limiting and caching** optimize performance.
- **AWS Lambda integration** showcases scalability and cloud event handling.



