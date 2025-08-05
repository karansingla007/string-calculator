# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy everything from current dir to container
COPY . /app

# Install required packages (pytest for testing)
RUN pip install --no-cache-dir pytest

# Default command to run when container starts
CMD ["pytest", "-v"]
