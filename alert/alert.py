import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='lightAlertQueue')

while True:
    method_frame, header_frame, body = channel.basic_get(queue='lightAlertQueue')
    if method_frame:
        print(f"[ALERT] {body.decode()}")
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    else:
        time.sleep(1)
