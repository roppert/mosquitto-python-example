#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
import paho.mqtt.client as paho

def on_message(mosq, obj, msg):
    print "%-20s %d %s" % (msg.topic, msg.qos, msg.payload)
    mosq.publish('pong', 'ack', 0)

def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect("127.0.0.1", 1883, 60)

    client.subscribe("kids/yolo", 0)
    client.subscribe("adult/#", 0)

    while client.loop() == 0:
        pass

# vi: set fileencoding=utf-8 :
