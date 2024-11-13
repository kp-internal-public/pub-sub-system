from src.consumer import Consumer
from src.service.message_service import MessageService
from src.topic import Topic


def run():

    c1 = Consumer("test1", lambda x: print(f"Consumer1 is print", x))
    c2 = Consumer("test2", lambda x: print(f"Consumer2 is print", x))

    service = MessageService()

    service.create_topic("topic1")
    service.add_consumer("topic1", c1)
    service.add_consumer("topic1", c2)

    service.send_message("topic1", "Hello world")
    service.send_message("topic1", "Hello world 1")
    service.send_message("topic1", "Hello world 2")

    service.remove_consumer("topic1", c1.id)

    print("--------------------REMOVE C1-----------------------------")

    service.send_message("topic1", "Hello world 3")
    service.send_message("topic1", "Hello world 4")
    service.send_message("topic1", "Hello world 5")
    service.send_message("topic1", "Hello world 6")

    print("--------------------ADD C1-----------------------------")
    service.add_consumer("topic1", c1)

    service.send_message("topic1", "Hello world 7")
    service.send_message("topic1", "Hello world 8")
    service.send_message("topic1", "Hello world 9")


run()
