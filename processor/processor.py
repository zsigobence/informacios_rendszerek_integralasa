import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='lightIntensityQueue')
channel.queue_declare(queue='lightAlertQueue')

low_light_count = 0

while True:
    method_frame, header_frame, body = channel.basic_get(queue='lightIntensityQueue')
    if method_frame:
        lux = int(body.decode())
        print(f"[<] Received lux value: {lux}")
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        
        if lux < 100:
            low_light_count += 1
            if low_light_count == 3:
                alert_msg = "Low light alert: 3 consecutive readings below 100 lux."
                channel.basic_publish(exchange='', routing_key='lightAlertQueue', body=alert_msg)
                print(f"[!] Alert sent: {alert_msg}")
                low_light_count = 0
        else:
            low_light_count = 0
    else:
        time.sleep(1)
