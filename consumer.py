from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "texts",
    # bootstrap_servers=["localhost:9092", "localhost:9093", "localhost:9094"],
    bootstrap_servers=["localhost:9092"],
    group_id="texts-consumer-group",
)

for message in consumer:
    print(message.value.decode())
