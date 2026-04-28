from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

# Dependency (DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------ CREATE ------------------
@router.post("/tasks")
def create_task(task: schemas.Task, db: Session = Depends(get_db)):
    db_task = models.TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# ------------------ GET ALL ------------------
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.TaskModel).all()

# ------------------ GET ONE ------------------
@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if not task:
        return {"Error": "Task not found"}
    return task

# ------------------ UPDATE ------------------
@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: schemas.UpdateTask, db: Session = Depends(get_db)):
    db_task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()

    if not db_task:
        return {"Error": "Task not found"}

    update_data = task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

# ------------------ DELETE ------------------
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()

    if not db_task:
        return {"Error": "Task not found"}

    db.delete(db_task)
    db.commit()
    return {"message": "Deleted successfully"}