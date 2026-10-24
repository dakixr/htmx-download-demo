# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir --require-hashes -r requirements.txt

# Copy project files
COPY . .
RUN useradd --uid 10001 --create-home app && chown -R app:app /app
USER app

# Expose port (default Flask port, can be changed via env)
EXPOSE 8000

# Start the app with gunicorn
CMD ["gunicorn", "main:app", "--timeout", "300", "--bind", "0.0.0.0:8000"] 
