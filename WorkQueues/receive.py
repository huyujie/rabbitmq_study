# -*- coding:utf-8 -*-

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     host='localhost'))
channel = connection.channel()

# declare queue is durable
channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    # release no response message
    ch.basic_ack(delivery_tag = method.delivery_tag)

# never send more than 1 message to receiver util it's handle the last message
channel.basic_qos(prefetch_count=1)

# no_ack default is False
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()

