# -*-coding:utf-8-*-

import pika

# build connection to server
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     host='127.0.0.1'))
channel = connection.channel()

# ensure queue has been build
channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
channel.start_consuming()
