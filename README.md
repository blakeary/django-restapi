# Wiki Web Application

This repository contains the Wiki Web Application developed with Django and Django REST Framework. The application provides a platform for creating and managing wiki pages on various topics.

## Setup

Follow these steps to set up the project on your local machine.

### Install Dependencies

Required dependencies:

```bash
pip install django
pip install djangorestframework
pip install python-decouple
pip install mysqlclient
```

Create a new Django project:

django-admin startproject webapp

Navigate to the project directory and create a new Django app:

cd webapp
django-admin startapp api

Create a .env file in your project root with your secret keys and database credentials:

# Secret key for Django

SECRET_KEY=your-secret-key

# AWS Credentials (if applicable)

AWS_ACCESS_KEY_ID=your-aws-access-key-id
AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key

# Database configuration

DATABASE_NAME=your-database-name
DATABASE_USER=your-database-user
DATABASE_PASS=your-database-password
DATABASE_HOST=your-database-host
DATABASE_PORT=your-database-port

To run the application, use:

python manage.py runserver

Before running the application, make sure to apply migrations:

python manage.py makemigrations
python manage.py migrate

The API will be available at:

http://127.0.0.1:8000/api/wiki
