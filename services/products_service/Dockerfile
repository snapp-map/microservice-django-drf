FROM python:3.12-slim

# Point of entry for the project
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# If you have a virtualenv in repo, you might skip it; else ensure no venv conflicts
# Make the entrypoint executable
RUN chmod +x docker-entrypoint.sh

# Use entrypoint for migrations and startup
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

# Production command with Gunicorn (adjust project path below)
CMD ["gunicorn", "users_service.wsgi:application", "--bind", "0.0.0.0:8000"]