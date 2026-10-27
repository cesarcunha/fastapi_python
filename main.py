from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/greet")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/users")
def create_user(user: User):
    return user

