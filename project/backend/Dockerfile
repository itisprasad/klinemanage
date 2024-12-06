# Use the Python slim image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to the container
COPY . /app

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

