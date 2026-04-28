# 🚀 Smart Task Manager API

A backend project built using **FastAPI** that implements full **CRUD (Create, Read, Update, Delete)** operations with a clean and modular architecture.

---

## 📌 Features

- ✅ Create Tasks  
- 📖 Read Tasks (Get all / Get by ID)  
- ✏️ Update Tasks  
- ❌ Delete Tasks  
- 🗄️ SQLite Database Integration  
- ⚡ FastAPI for high performance APIs  
- 🧱 Structured backend design (routes, schemas, models)

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**

---

## ▶️ How to Run

```bash
cd backend
uvicorn app.main:app --reload
📖 API Documentation

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

Use the Swagger UI to test all API endpoints.
🧪 API Endpoints
Method	Endpoint	Description
POST	/tasks	Create a task
GET	/tasks	Get all tasks
GET	/tasks/{id}	Get task by ID
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task
📌 What I Learned
Building REST APIs using FastAPI
Implementing CRUD operations
Structuring scalable backend projects
Using SQLAlchemy for database operations
Managing request validation with Pydantic
🚀 Future Improvements
🔐 Add JWT Authentication
🌐 Connect Frontend (React)
☁️ Deploy API online
👩‍💻 Author

Archana Surawi
GitHub: https://github.com/achu-narayana
