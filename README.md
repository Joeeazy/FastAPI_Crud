# FastAPI Task Management API

This project is a simple Task Management API built using FastAPI. It allows you to create, read, update, and delete tasks. FastAPI automatically generates interactive API documentation at `http://127.0.0.1:8000/docs`, which you can use to test the endpoints.

## Features

- **Create a new task**
- **Read all tasks**
- **Read a single task by ID**
- **Update a task by ID**
- **Delete a task by ID**

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:

   ```bash
   git clone
   cd

   ```

2. Create and activate a virtual environment:

   python -m venv env
   source env/bin/activate # On Windows, use `env\Scripts\activate`

3. Install the dependencies:

   windows - pip install fastapi uvicorn pydantic

   MacOS - pip3 install fastapi uvicorn pydantic

# Running the API

    Run the FastAPI server:

    python main.py

    The server will start at http://127.0.0.1:8000.

    Open your browser and navigate to http://127.0.0.1:8000/docs to view and interact with the API documentation.

# Code Overview

    main.py

    This is the main file that sets up the FastAPI app and defines the API endpoints.

    # Imports:

    FastAPI and HTTPException from fastapi

    BaseModel from pydantic

    List, Optional from typing

    UUID, uuid4 from uuid

    # Models:

    Task model using BaseModel from Pydantic.

    # In-memory Database:

    A list named tasks to store task objects.

    # Endpoints:

    * create_task: Create a new task.

    * read_tasks: Read all tasks.

    * read_task: Read a specific task by ID.

    * update_task: Update a task by ID.

    * delete_task: Delete a task by ID.


    # Run the API:

    Use uvicorn to run the app.
