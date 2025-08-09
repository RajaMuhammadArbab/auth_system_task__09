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

## Project Demo

<img width="1370" height="653" alt="admin" src="https://github.com/user-attachments/assets/136109a7-bd4c-44b4-9bd5-6262bc9e2721" />
<img width="1382" height="682" alt="login" src="https://github.com/user-attachments/assets/ada7a809-d8b3-409b-9667-0917d28f2601" />
<img width="1369" height="579" alt="content" src="https://github.com/user-attachments/assets/7261810e-ef32-433a-8cfb-1e590059e96d" />
<img width="1380" height="579" alt="content_delete" src="https://github.com/user-attachments/assets/1dd0ad4c-5558-46dd-bc9c-7859a9919b33" />
<img width="1376" height="587" alt="get_content" src="https://github.com/user-attachments/assets/1064078c-5868-4f7a-8a35-ab81af1bc5d0" />
<img width="1368" height="691" alt="getuser" src="https://github.com/user-attachments/assets/a97f34d1-afd6-40d5-a00e-e5569c029c50" />
