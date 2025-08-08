#  Django Authentication System with PostgreSQL

A simple Django REST API for user authentication using JWT and PostgreSQL.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/auth_system.git
cd auth_system
```

---

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

---

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

> Make sure `requirements.txt` contains:
> ```
> django
> djangorestframework
> psycopg2-binary
> djangorestframework-simplejwt
> ```

---

### 4. Configure PostgreSQL Database

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 7. Run Development Server

```bash
python manage.py runserver
```

---

##  Test API Endpoints

Use [Postman](https://www.postman.com/) to test:

### Register

- **POST** `/api/register/`
- **Body (JSON)**:

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "TestPass123"
}
```

---

##  Token Authentication (if implemented)

- **POST** `/api/token/`  
```json
{
  "username": "testuser",
  "password": "TestPass123"
}
```

- **POST** `/api/token/refresh/`  
```json
{
  "refresh": "<your_refresh_token>"
}
```

---

##  Project Structure

```
auth_system/
│
├── auth_system/       # Project settings
├── users/             # Custom app for user authentication
├── manage.py
└── requirements.txt
```

---

