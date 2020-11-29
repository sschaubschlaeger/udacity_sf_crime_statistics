import asyncio
from confluent_kafka import Consumer


async def consume(topic_name):
    consumer = Consumer({
        "bootstrap.servers": "PLAINTEXT://localhost:9092",
        "group.id": "police-calls",
    })
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume()
        for message in messages:
            if message.error() is not None:
                print(f"Error: {message.error()}")
            else:
                print(f"{message.value()}\n")
                
        await asyncio.sleep(1.0)
                
def run_consumer():
        asyncio.run(consume("com.udacity.police-calls"))

        
if __name__ == '__main__':
    run_consumer()