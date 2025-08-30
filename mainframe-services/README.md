# FastAPI Backend Project

This project is a FastAPI-based backend application with MongoDB integration. It provides a robust structure for building scalable and maintainable web applications.

## Features

- User authentication and authorization
- Project management
- Repository handling
- Assessment system
- Reverse engineering capabilities
- Chat functionality
- Background task processing

## Prerequisites

- Python 3.10+
- MongoDB 8.0+
- Poetry 1.8.4+

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install Poetry if you haven't already:
   ```
   curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4
   ```

3. Install the project dependencies:
   ```
   poetry install
   ```

4. Set up your environment variables by creating a `.env` file in the root directory:
   ```
   APP_NAME="Your API Name"
   DEBUG_MODE=True
   DATABASE_URL="mongodb://localhost:27017"
   DATABASE_NAME="your_database_name"
   SECRET_KEY="your-secret-key"
   ALGORITHM="HS256"
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

## Running the Application

To run the application, use the following command:
   ```
   PYTHONPATH=app/ poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```