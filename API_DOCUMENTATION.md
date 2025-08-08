#  API Documentation - Django Authentication System

##  Authentication Routes

### POST `/api/register/`
Registers a new user.

#### Request Body (JSON)
```
{
  "username": "exampleuser",
  "email": "user@example.com",
  "password": "examplepassword"
}
```

#### Response (201 Created)
```
{
  "message": "User registered successfully!"
}
```

---

### POST `/api/token/`
Obtain JWT access and refresh tokens.

#### Request Body (JSON)
```
{
  "username": "exampleuser",
  "password": "examplepassword"
}
```

#### Response (200 OK)
```
{
  "refresh": "jwt_refresh_token",
  "access": "jwt_access_token"
}
```

---

### POST `/api/token/refresh/`
Refresh the JWT access token.

#### Request Body (JSON)
```
{
  "refresh": "jwt_refresh_token"
}
```

#### Response (200 OK)
```
{
  "access": "new_jwt_access_token"
}
```

---

##  Setup

- All endpoints use JWT for authentication.
- Include the access token in the `Authorization` header:
```
Authorization: Bearer <access_token>
```
