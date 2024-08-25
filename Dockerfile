# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY etl_pipeline.py /app/
COPY requirements.txt /app/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the script
CMD ["python", "etl_pipeline.py"]
