import bisect
import collections
from typing import List

from .consumer import Consumer, Dict, Message


class Topic:
    def __init__(self, id) -> None:
        self.id = id
        self.consumers: Dict[int, Consumer] = {}
        self.message_ids: List[int] = []
        self.messages: List[Message] = []

    def add_consumer(self, consumer: Consumer):
        self.consumers[consumer.id] = consumer

    def remove_consumer(self, id):
        del self.consumers[id]

    def send_message(self, message: Message):
        self.message_ids.append(message.id)
        self.messages.append(message)

        self.notify_consumers()

    def notify_consumers(self):
        if not self.messages:
            return
        for consumer in self.consumers.values():
            last_message_id = consumer.get_last_message_id(self.id)
            if not last_message_id:
                consumer.__call__(self.id, self.messages[-1])
                continue

            if last_message_id != self.messages[-1].id:
                # consumer out of last message
                start_index = bisect.bisect_left(self.message_ids, last_message_id) + 1
                for i in range(start_index, len(self.messages)):
                    consumer.__call__(self.id, self.messages[i])
