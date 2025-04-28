import pika
import random
import time

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        break
    except pika.exceptions.AMQPConnectionError:
        print(" [!] Waiting for RabbitMQ to be ready...")
        time.sleep(3)

channel = connection.channel()
channel.queue_declare(queue='lightIntensityQueue')

while True:
    lux = random.randint(0, 2000)
    channel.basic_publish(exchange='', routing_key='lightIntensityQueue', body=str(lux))
    print(f"[>] Sent lux value: {lux}")
    time.sleep(3)
