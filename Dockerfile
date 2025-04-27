# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (default Flask port, can be changed via env)
EXPOSE 8000

# Start the app with gunicorn
CMD ["gunicorn", "main:app", "--timeout", "300", "--bind", "0.0.0.0:8000"] 