# 🍬 Sweet Shop Management System

A full-stack Sweet Shop Management System built as part of a **time-bound (24-hour) technical assessment**. The project demonstrates backend API design, authentication, database integration, and a basic frontend setup using modern web technologies.

---

## 📌 Project Overview

The Sweet Shop Management System allows users to register, log in, and interact with a sweets inventory. The backend exposes RESTful APIs secured with JWT authentication, while the frontend provides a basic interface to interact with these APIs.

This project was designed to showcase:

* Backend architecture and API structuring
* Authentication and authorization concepts
* Database modeling
* Frontend–backend integration
* Clean project organization under strict time constraints

---

## 🛠 Tech Stack

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **SQLite** (development database)
* **JWT Authentication**
* **Uvicorn**

### Frontend

* **React**
* **Vite**
* **JavaScript**
* **Axios**

---

## ✨ Features Implemented

### Authentication

* User registration
* User login
* JWT-based authentication

### Backend Structure

* Modular FastAPI project layout
* Database models and schemas
* API routing separation
* Environment-based configuration support

### Frontend

* Basic project setup with React + Vite
* Authentication pages (login/register)
* API integration layer

---

## 🚧 Partially Implemented / Planned Features

Due to the **24-hour time limit**, the following features are planned but not fully completed:

* Full CRUD operations for sweets
* Search and filter functionality
* Purchase and restock logic
* Role-based access (Admin vs User)
* Automated unit and integration tests
* Polished UI/UX

These items are documented intentionally to reflect honest project status and prioritization.

---

## ⏱ Time Constraint Disclosure

> ⚠️ **Important Note**
>
> This project was completed within a strict **24-hour timeframe** as part of a hiring assessment.
>
> Given the limited time, priority was given to:
>
> * Correct project structure
> * Backend foundation and authentication flow
> * Database integration
>
> Non-critical features such as full CRUD completion, extensive testing, and UI polish were intentionally deferred and documented for future work.

---

## ▶️ How to Run the Project Locally

### Prerequisites

* Python 3.10+
* Node.js 18+
* Git

---

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at:

```
http://localhost:3000
```

---

## 📂 Project Structure

```
sweet_project/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── security.py
│   │   ├── deps.py
│   │   └── routers/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🤖 My AI Usage

AI tools were used responsibly during development to improve productivity and understanding.

### Tools Used

* **ChatGPT**

### How AI Was Used

* Clarifying FastAPI and JWT authentication concepts
* Debugging runtime errors and configuration issues
* Structuring project folders and files
* Improving README documentation clarity

### Reflection
AI helped accelerate learning and problem-solving but all implementation decisions, debugging, and final code understanding were done manually. The project reflects my own learning and effort, supported by AI as a productivity tool.

## 📈 Future Improvements
With additional time, the following enhancements would be implemented:

* Complete sweets inventory management
* Admin dashboard
* Comprehensive test suite (pytest)
* Improved frontend UI/UX
* Deployment to cloud platform
