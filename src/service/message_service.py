from typing import List

from ..consumer import Consumer
from ..message import Message
from ..topic import Topic


class MessageService:
    def __init__(self) -> None:
        self.topics = {}
        self.current_key = 0

    def create_topic(self, id):
        if id in self.topics:
            raise Exception("Already exist")

        topic = Topic(id)
        self.topics[id] = topic

    def list_topics(self) -> List[Topic]:
        return list(self.topics.values())

    def get_topic_by_id(self, id) -> Topic:
        return self.topics[id]

    def add_consumer(self, topic_id, consumer: Consumer):
        topic = self.get_topic_by_id(topic_id)
        topic.add_consumer(consumer)

        topic.notify_consumers()

    def remove_consumer(self, topic_id, consumer_id):
        self.get_topic_by_id(topic_id).remove_consumer(consumer_id)

    def send_message(self, topic_id, data):
        self.current_key += 1
        message = Message(self.current_key, data)
        topic = self.get_topic_by_id(topic_id)
        topic.send_message(message)
