import os
import time
import random
import json
import openai
from kafka import KafkaProducer

# Load environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")
KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
TOPIC = os.environ.get("KAFKA_TOPIC", "events")

# Initialize Kafka producer with JSON serialization.
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def generate_event():
    """
    Calls the OpenAI API to generate a dynamic event.
    Adjust the prompt and parameters as needed for your use case.
    """
    prompt = (
        "Generate a dynamic event from the following list: "
        "traffic congestion, server attack, power outage, natural disaster."
    )
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=10,
            n=1,
            temperature=0.8
        )
        event_text = response.choices[0].text.strip()
        return {"event": event_text, "timestamp": time.time()}
    except Exception as e:
        print("Error generating event:", e)
        return None

def main_loop():
    """
    Main loop that generates and publishes events continuously.
    Randomized sleep simulates bursty load.
    """
    print("Event generator started.")
    while True:
        event = generate_event()
        if event:
            try:
                producer.send(TOPIC, value=event)
                print("Event published:", event)
            except Exception as e:
                print("Error publishing event to Kafka:", e)
        # Adjust sleep time to simulate bursty behavior
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    main_loop()
