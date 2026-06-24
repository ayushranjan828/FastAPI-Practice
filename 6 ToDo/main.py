from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
            "Message": "ToDo added", 
            "Data":todo
            }

@app.get("/todos")
def get_todo():
    return todos

@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"Message": "ToDo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[idx] = updated_todo
            return {
                    "Message": "ToDo updated", 
                    "Data":updated_todo
                    }
    return {"Message": "ToDo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(idx)
            return {"Message": "ToDo deleted"}
    return {"Message": "ToDo not found"}