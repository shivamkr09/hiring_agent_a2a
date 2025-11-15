# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port 8080
EXPOSE 8080

# Set working directory to basic_agent
WORKDIR /app/basic_agent

# Run the application with PORT environment variable support for Azure
CMD ["sh", "-c", "adk api_server --host=0.0.0.0 --port=${PORT:-8080} --allow_origins=*"]
