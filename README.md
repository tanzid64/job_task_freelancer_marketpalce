
# TASK-FREELANCER-MARKETPLACE [BACK END DEVELOPER]
## Overview

Develop the backend of a web application that serves as a freelancing marketplace. The
project will focus on secure user management, role-based access control, and basic job
management..

---

## Table of Contents
- [API Endpoints](#api-endpoints)
  - [User](#user)
  - [Jobs](#jobs)
- [API Documentation](#api-documentation)
- [Project Installation Guide](#project-installation-guide)

---
## API Endpoints

### **User**
- **Register**: `POST /api/v1/auth/users/`
- **Email Activation**: `POST /api/v1/auth/users/activation/`
- **Resend Activation Email**: `POST /api/v1/auth/users/resend_activation/`
- **Login**: `POST /api/v1/auth/login/`
- **Get User Profile**: `GET /api/v1/auth/users/me/`
- **Token Refresh**: `POST /api/v1/auth/token/refresh/`
- **Verify Token**: `POST /api/v1/auth/token/verify/`
- **Update User Profile**: `PATCH /api/v1/auth/users/me/`
- **Delete an user**: `DELETE /api/v1/auth/users/me/`
- **Change Password**: `POST /api/v1/auth/users/set_password`
- **Reset Password**: `POST /api/v1/auth/users/reset_password/`
- **Reset Password Confirmation**: `POST /api/v1/auth/users/reset_password_confirm/`
- **Update user's email**: `POST /api/v1/auth/users/set_email/`

### **Jobs**
- **Create Job**: `POST /api/v1/jobs/`
- **Get Jobs List**: `GET /api/v1/jobs/`
- **Get Job Details**: `GET /api/v1/jobs/{job_slug}/`
- **Update Job Details**: `PATCH /api/v1/jobs/{job_slug}/`
- **Delete Job**: `/api/v1/jobs/{job_slug}/`
---

## API Documentation

- **Swagger API Documentation**: `GET /api/v1/documentation/`
- **Download Schema**: `GET /api/v1/schema/`
- **Postman API Documentation**: `GET /api/v1/schema/`

---


### Project Installation Guide

Clone the repo and go to the project root.
```bash
git clone https://github.com/tanzid64/job_task_freelancer_marketpalce.git
```
```bash
cd 
```
**Docker Setup**

```bash
sudo docker compose up --build --remove-orphans -d
```
***Bash***
```bash
sudo docker exec -it <container name> bash
```
***Logs***
```bash
sudo docker logs <container name>
```

**Local Machine Setup**
```bash
virtualenv .venv
```
```bash
source .venv/bin/activate
```
***Set up the .env file***

`.env.example > .env`

In your `.env` set the following environment variables:

- `SECRET_KEY` : Your Secret Key.
- `DEBUG` : True / False.
- `DATABASE_URL` : Your Postgres Database URL.

```bash
python manage.py migrate
```
***To run test cases***
```bash
python manage.py test
```
***Run server***
```bash
python manage.py runserver
```
