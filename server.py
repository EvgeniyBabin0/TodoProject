from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import create_task, delete_task, get_all_tasks, get_task, update_task

app = FastAPI()

class TaskIn(BaseModel):
    title: str
    completed: bool = False

class TaskOut(TaskIn):
    id: str

@app.get("/tasks", response_model=list[TaskOut])
def api_get_tasks():
    tasks = get_all_tasks()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskOut)
def api_get_task(task_id: str):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=TaskOut)
def api_create_task(task: TaskIn):
    task_dict = task.model_dump()
    new_task = create_task(task_dict)
    return new_task

@app.put("/tasks/{task_id}", response_model=TaskOut)
def api_update_task(task_id: str, task: TaskIn):
    updated = update_task(task_id, task.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = get_task(task_id)
    return updated_task

@app.delete("/tasks/{task_id}")
def api_delete_task(task_id: str):
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
