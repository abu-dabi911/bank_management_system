<<<<<<< HEAD
# Bank Management System

## 📌 Project Description
This project is a **bank management system** developed using **Django**, **PostgreSQL**, and **Django Authentication**. It includes **user registration, authentication, role-based access, and secure data storage**.

## 🚀 Features
✔ **User Registration & Authentication** (login, logout, session protection)  
✔ **Role-based Access** (admin/customer)  
✔ **Password Hashing** (PBKDF2 + SHA256)  
✔ **PostgreSQL Database Connection**  
✔ **Django Admin Panel for management**  
✔ **Django Templates for frontend**  

---

## 📂 Project Structure

```
bank-management-system/
│── bank_app/
│   ├── migrations/        # Database migration files
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, JS, images
│   ├── views.py           # Login / Registration logic
│   ├── models.py          # Database models (Customer, Account)
│   ├── urls.py            # App routes
│   ├── forms.py           # Django Forms
│   ├── admin.py           # Django Admin
│── bank_management_system/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main routes
│   ├── wsgi.py            # Project startup
│── manage.py              # Main management script
```

---

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/username/bank-management-system.git
cd bank-management-system
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL Database
1. Open PostgreSQL and create a database:
```sql
CREATE DATABASE bank_db;
```
2. Update `settings.py` with:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bank_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Apply Migrations and Start Server
```bash
python manage.py makemigrations bank_app
python manage.py migrate
python manage.py createsuperuser  # Create admin user
python manage.py runserver
```

Now, visit [127.0.0.1:8000](http://127.0.0.1:8000/)

---

## 🖥 Main URLs
📌 **Home Page** → `http://127.0.0.1:8000/`
📌 **Login Page** → `http://127.0.0.1:8000/login/`
📌 **Register Page** → `http://127.0.0.1:8000/register/`
📌 **Logout** → `http://127.0.0.1:8000/logout/`
📌 **Django Admin Panel** → `http://127.0.0.1:8000/admin/`

---

## 🔐 Security Features
✔ **Django Authentication System**  
✔ **Passwords are securely hashed** (PBKDF2 + SHA256)  
✔ **CSRF Protection and SQL Injection Prevention**  
✔ **Secure Session Management**  

---

## ✅ To-Do (Future Enhancements)
- [ ] Add "Forgot Password?" feature
- [ ] Add User Profile Page
- [ ] Develop API for Mobile Integration

📌 **Author**: [Abdugaffar Omerbek]  
📌 **GitHub**: [Repository Link]

=======
# bank_management_system
>>>>>>> a677628db52823daca38e725b7c8fa227505e43e
