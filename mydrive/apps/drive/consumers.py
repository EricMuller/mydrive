# coding: utf8
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Channel
from json import dumps
from channels import Group
# from pprint import pprint
from channels.sessions import channel_session
# import json
import datetime


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse(
        "Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


class Content:
    def __init__(self, reply_channel):
        self.reply_channel = reply_channel

    def send(self, json):
        Channel(self.reply_channel).send({'content': dumps(json)})


class Message:
    def __init__(self, message):
        self.message = message

    def as_dict(self):
        return self.__dict__


@channel_session
def ws_receive(message):
    print(' Server received websocket data.' + str(datetime.datetime.now()))
    room = message.content['path'].strip("/")
    print(message.content['text'])
    Group(room).send({'text': message.content['text']})


@channel_session
def ws_connect(message):
    # pprint(vars(message.reply_channel))
    room = message.content['path'].strip("/")
    Group(room).add(message.reply_channel)

    # Group(room).send({'text': message.content['text']})


@channel_session
def ws_disconnect(message):
    room = message.content['path'].strip("/")
    Group(room).discard(message.reply_channel)


class WsPublisher:

    def __init__(self, room=None):
        if room is not None:
            self.room = room
        else:
            self.room = 'ws'

    def ws_send(self, event, data):
        print('ROOM:' + self.room)
        text = {"event": event, "data": data}
        print(text)
        Group(self.room).send({'text': dumps(text)})
