# 🚀 Lucid Posts - FastAPI MVC Web Application

Lucid Posts is a **FastAPI-based web application** that follows the **Model-View-Controller (MVC)** design pattern. It includes **user authentication (JWT)**, **post management**, **SQLAlchemy ORM**, **in-memory caching**, and **extensive validation**.

## 📌 Features
✅ **User Authentication** (Signup/Login with JWT)  
✅ **Token-based Authentication**  
✅ **CRUD Operations on Posts**  
✅ **Field Validation with Pydantic**  
✅ **Database Integration with MySQL (SQLAlchemy)**  
✅ **Middleware for Authentication**  
✅ **In-Memory Caching for Performance Optimization**  

## 🚀 Tech Stack
- **FastAPI** - Web framework  
- **SQLAlchemy** - ORM for MySQL  
- **JWT** - Authentication  
- **Pydantic** - Data validation  
- **Alembic** - Database migrations  
- **Cachetools** - In-memory caching  
- **Passlib** - Password hashing  

## ⚙️ Installation & Setup


### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd <project-folder>
```

### 2️⃣ Clone the Repository
```bash
python -m venv venv
```

```bash
source venv/bin/activate   # Mac/Linux
```
```bash
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a .env file and add the following variables:

DATABASE_URL=mysql+pymysql://username:password@localhost/db_name
SECRET_KEY=your_secret_key

### 5️⃣ Apply Migrations
```bash
alembic upgrade head
```
### 6️⃣ Run the Application
```bash
uvicorn app.main:app --reload
```

### 7️⃣ Access API Documentation
Once the application is running, FastAPI provides interactive API documentation at:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

These interfaces allow you to test the API endpoints easily.


✨ Author
👨‍💻 Developed by Biniyam Abiy Tirfe