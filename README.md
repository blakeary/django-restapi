# Wiki Web Application

This repository contains the Wiki Web Application developed with Django and Django REST Framework. The application provides a platform for creating and managing wiki pages on various topics.

## Setup

### Configuring the Environment

1. **Create a `.env` file**: In the root of your project, create a `.env` file to store your environment variables.

2. **Add Environment Variables**: Include the following variables in your `.env` file. Replace the placeholder values with your actual database and secret key information.

    ```
    SECRET_KEY=your-secret-key
    DATABASE_NAME=your-database-name
    DATABASE_USER=your-database-user
    DATABASE_PASS=your-database-password
    DATABASE_HOST=your-database-host
    DATABASE_PORT=your-database-port
    ```

### Running the App Locally

1. **Install Dependencies**: First, install the required dependencies:

    ```bash
    pip install django
    pip install djangorestframework
    pip install python-decouple
    ```

2. **Run Migrations**: Set up your database by running the migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Start the Server**: To start the local development server:

    ```bash
    python manage.py runserver
    ```

### Building and Running with Docker

1. **Build the Docker Image**:

    ```bash
    docker build -t django-restapi .
    ```

2. **Run the Docker Container**:

    ```bash
    docker run -p 8000:8000 django-restapi
    ```

## API Endpoints

The application offers the following RESTful APIs:

-   **Login User**: `POST http://127.0.0.1:8000/api/login`
-   **Register User**: `POST http://127.0.0.1:8000/api/register`
-   **Get All Pages**: `GET http://127.0.0.1:8000/api/get-pages`
-   **Get Page by Id**: `GET http://127.0.0.1:8000/api/get-page/{id}`
-   **Create Page**: `POST http://127.0.0.1:8000/api/create-page`
-   **Update Page**: `PUT http://127.0.0.1:8000/api/update-page/{id}`
-   **Partial Update Page**: `PATCH http://127.0.0.1:8000/api/partial-update-page/{id}`
-   **Delete Page**: `DELETE http://127.0.0.1:8000/api/delete-page/{id}`

Replace `{id}` with the actual ID of the page for the relevant API calls.
