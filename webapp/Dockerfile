# For AWS deployment - from https://hub.docker.com/_/python
# FROM --platform=linux/amd64 python:3.11-bookworm

# For local deployment - from https://hub.docker.com/_/python
FROM python:3.11-bookworm

# Set the environment variable PYTHONUNBUFFERED to 1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /django
WORKDIR /django

# Copy requirements.txt from the current directory to /django, run pip freeze > requirements.txt prior
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /django
COPY . .

# Run app.py when the container launches
CMD python manage.py runserver 0.0.0.0:8000

# Expose port 8000 for reverse proxy in nginx
EXPOSE 8000