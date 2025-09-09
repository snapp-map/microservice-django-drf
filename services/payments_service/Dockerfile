# Base image: Python 3.12 (slim)
FROM python:3.12-slim

# Do not buffer Python output
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN python -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project code
COPY . .

# Ensure docker-entrypoint.sh is executable (set permissions locally if needed)
# Run entrypoint, then Django server
CMD ["bash", "docker-entrypoint.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]