from fastapi import FastAPI
from app.routes import task_routes

app = FastAPI()

app.include_router(task_routes.router)
@app.get("/")
def home():
    return {"message": "API is running 🚀"}