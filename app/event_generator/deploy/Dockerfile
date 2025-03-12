FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the event generator service
CMD ["python", "event_generator.py"]
