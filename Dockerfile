# Base image
FROM python:3.8-slim-buster

# Debian Package Installing
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    apt-utils \
    apt-transport-https \
    debconf-utils \
    gcc \
    g++ \
    build-essential \
    unixodbc-dev \
    unixodbc \
    libpq-dev

# Removing Debian Package Cache
RUN rm -rf /var/lib/apt/lists/*

# Set web server root as working directory
WORKDIR /home/site/wwwroot

# Install required packages
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose port 8000
EXPOSE 8000

# Start flask app using Gunicorn
CMD gunicorn --workers 4 --threads=2 --bind 0.0.0.0:8000 app:app
