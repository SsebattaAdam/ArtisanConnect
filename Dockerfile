# Use an official Python runtime as a base image
FROM python:3.11-slim


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Install system dependencies for mysqlclient and psycopg2
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    libpq-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file to install dependencies first
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Run Django application
CMD ["python", "artisanProject/manage.py", "runserver", "0.0.0.0:8000"]
