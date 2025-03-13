FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY ../../ .

RUN ls -la
# install deps and build
RUN ./scripts/build.sh

# Run the event generator service
CMD ["python3", "-m", "event_generator"]
