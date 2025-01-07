
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
- **Postman API Documentation**: `https://documenter.getpostman.com/view/32603042/2sAYJAeHfX`

---


### Project Installation Guide

Clone the repo and go to the project root.
```bash
git clone https://github.com/tanzid64/project-management-techforing.git
```
***Setup .env file***
- `SECRET_KEY` : 
- `DEBUG` : 
- `DATABASE_URL` : 
- `EMAIL_HOST` : 
- `EMAIL_HOST_USER` : 
- `EMAIL_HOST_PASSWORD` : 
- `EMAIL_PORT` : 

**Docker Setup**
---
***if your machine supports Makefile***
***Build***
```bash
make build
```
***Up***
```bash
make up
```
***Down***
```bash
make down
```
***Show Logs***
```bash
make logs
```
***Show App Logs***
```bash
make show-logs-api
```
***Access App Terminal***
```bash
make bash-api
```
---
***if your machine doesn't supports Makefile***
***Build***
```bash
docker compose -f docker-compose.yml up --build -d --remove-orphans
```
***Up***
```bash
docker compose -f docker-compose.yml up -d
```
***Down***
```bash
docker compose -f docker-compose.yml down
```
***Show Logs***
```bash
docker compose -f docker-compose.yml logs
```
***Show App Logs***
```bash
docker compose -f docker-compose.yml logs api
```
***Access App Terminal***
```bash
docker exec -it freelancer_marketplace_api bash
```
---

---
**Local Machine Setup**
```bash
virtualenv .venv
```
```bash
source .venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
---
***To Seed Database***
```bash
python manage.py seed_users
```
```bash
python manage.py seed_jobs
```
Db seed user's password: example@123
Db seed user admin: admin1@example.com
Db seed user admin password: admin@123

***Create Superuser***
```bash
python manage.py createsuperuser
```
***Run server***
```bash
python manage.py runserver
```
---

### Dev Server Info
---
Link: https://job-task-freelancer-marketpalce.onrender.com