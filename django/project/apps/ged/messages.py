
from rest_framework import serializers


class Message():

    def __init__(self, code, message):
        self.code = code
        self.message = message


class MessageSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    message = serializers.CharField(max_length=30)

    class Meta:
        model = Message
        fields = (
            'code', 'message')
