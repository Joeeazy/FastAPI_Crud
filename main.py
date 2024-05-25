from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4


# create a new instance of FastAPI
app = FastAPI()

# create a class model to represent different tasks
class Task(BaseModel):
    #define all the fields with their data type
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completedt: bool = False


# temporary in-memory database 
tasks = []


#route to create a new task response model is the Task Pydantic model 
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4() # a new unique id 
    tasks.append(task) #    append to tasks in memory db
    return task



# create a route to read the tasks
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks



# endpoint to view a paticular task
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    # check for task_id
    for task in tasks:
        # if present return the task
        if task.id == task_id:
            return task
        # else return an exception 404 not found
    raise HTTPException(status_code=404, detail="Task Not Found!")



# endpoint to update a task PUT
@app.put("/tasks/{task_id}", response_model=Task)
# look for task with task_id and update it parameters
def update_task(task_id:UUID, task_update: Task):
    # enumarate gets both the index and task
    for index, task in enumerate(tasks):
        if task.id == task_id:
            # check for new fiels task_update get its dictionary representation and exclude any unset fields
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[index] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


# endpoint to delete a task
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    # loop in tasks get index if id matches pop the task
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(index)
    # if id does not exist raise exception
    raise HTTPException(status_code=404, detail="Task not found")

# run the api
if __name__ == "__main__":
    import uvicorn # web server that allows running of the api

    uvicorn.run(app, host="0.0.0.0", port=8000)