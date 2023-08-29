import time
from kafka import KafkaProducer
from faker import Faker

fake = Faker()
producer = KafkaProducer(
    # bootstrap_servers=["localhost:9092", "localhost:9093", "localhost:9094"]
    bootstrap_servers=["localhost:9092"]
)
for _ in range(100):
    new_text = fake.text()
    producer.send("texts", new_text.encode("utf-8"))
    print(new_text)
    time.sleep(1)
time.sleep(20)
