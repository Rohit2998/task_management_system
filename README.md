# Task Management API

## Overview
This project is a simple Task Management API built using **Django** and **Django REST Framework**. It provides endpoints to perform CRUD operations on tasks, assign tasks to users, and filter tasks based on their status. The project also integrates **rate-limiting**, **caching with Redis**, and **AWS Lambda simulation** for task notifications.

## Requirements

### Framework
- **Python** with **Django** and **Django REST Framework**.

### Features
- **CRUD API** for tasks (Create, Read, Update, Delete).
- **User authentication** (Token-based or Django’s built-in auth).
- **Task filtering** by status (e.g., `pending`, `completed`).
- **Rate-limited API endpoint**:
  - Uses Django’s built-in features or a lightweight caching mechanism (Redis-like logic).
  - Unit test included for rate-limiting.
- **Database**:
  - PostgreSQL schema compatible with AWS Aurora DB.
  - Implemented using Django ORM.
- **AWS Integration**:
  - Simulated AWS Lambda function (local script) that sends a notification when a task is marked as `completed`.
  - Uses environment variables or a config file for AWS-like service integration.
- **Bonus**: Auto-scaling logic for an EC2-like environment based on task volume (optional).

## Installation & Setup

### Prerequisites
- Python 3.10+
- Docker & Docker Compose

### Steps
1. **Clone the Repository**
   ```sh
   git clone <repo_url>
   cd task-management-api
   ```

2. **Set up a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Start the Server**
   ```sh
   python manage.py runserver
   ```

6. **Run in Docker** (Recommended)
   ```sh
   docker-compose up --build
   ```

## API Endpoints

| Method | Endpoint          | Description          | Auth Required |
|--------|------------------|----------------------|--------------|
| POST   | `/api/register/`  | Create a new user   | No           |
| POST   | `/api/token/`     | Get authentication token | No   |
| GET    | `/api/tasks/`     | List all tasks      | Yes          |
| POST   | `/api/tasks/`     | Create a task       | Yes          |
| GET    | `/api/tasks/{id}/` | Retrieve a task    | Yes          |
| PUT    | `/api/tasks/{id}/` | Update a task      | Yes          |
| DELETE | `/api/tasks/{id}/` | Delete a task      | Yes          |

## AWS Lambda Simulation
- A simulated AWS Lambda function logs a message when a task is marked as `completed`.
- It can be triggered using a local script to mimic real AWS Lambda invocation.

## Database Schema (PostgreSQL)
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(10) CHECK (status IN ('pending', 'completed')) DEFAULT 'pending',
    assigned_to INTEGER REFERENCES auth_user(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Testing
- Run tests using:
  ```sh
  python manage.py test
  ```
- Includes unit tests for **rate-limiting logic**.

## Scalability Considerations
- **Dockerized environment** for easy deployment.
- **Redis caching** to reduce database load.
- **AWS Lambda simulation** for event-driven notifications.
- **Potential EC2 auto-scaling** (future enhancement).

## Evaluation Criteria
- Code quality (readability, PEP 8 compliance).
- Proper use of Django ORM and RESTful principles.
- Well-structured SQL schema with indexing considerations.
- AWS concepts (Lambda integration, scalability).
- Detailed documentation for ease of use.

---

For any issues or contributions, feel free to submit a pull request or open an issue! 🚀

