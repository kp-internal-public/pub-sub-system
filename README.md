Implement a persistent pub-sub queue mechanism1 with guaranteed delivery of every published message for all the subscribed consumers in that subscribed topic in the same order.

Features:
API to expose topics
API for publisher to push messages against a topic
API to subscribe and unsubscribe from topic
API for subscriber to consume from topic
Maintain the state of consumption of each message in each topic for each consumer.
Maintain order of message consumption for each consumer.
Handle cases of consumers not being available. What to do with those messages? (Write to disk and restore?)
Filtered message consumption in a topic by the consumer


# Topic, Consumer, Publisher
# Map { topicId: lastMessageId }

# TOPIC -> Consumer
# Consumer -> unsubscribe, re-subscription

# WAL
