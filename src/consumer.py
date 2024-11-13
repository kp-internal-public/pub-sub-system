from collections import defaultdict
from typing import Any, Dict

from .message import Message


class Consumer:
    def __init__(self, id, fn) -> None:
        self.topic_message: Dict[Any, int] = defaultdict(int)  # int: int
        self.id = id
        self.fn = fn

    def get_last_message_id(self, topic_id: int):
        return self.topic_message[topic_id]

    def __call__(self, topic_id, message: Message):
        self.topic_message[topic_id] = message.id
        self.fn(message)
