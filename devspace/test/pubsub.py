import os
import json
import logging

from retry import retry
from google.cloud import pubsub_v1 as pubsub
from google.api_core.exceptions import AlreadyExists


logger = logging.getLogger(__name__)


# SECTION -  Test Pubsub emulators connections
class PubSubClient(object):
    def __init__(self, project, cache=None):
        self._project_id = project
        self.publisher, self.subscriber = self._get_clients()

    @retry(tries=3, delay=1, logger=logger)
    def publish_message(self, topic_name, message):
        body = json.dumps(message).encode('utf-8')
        try:
            self.publisher.publish(topic_name, body,
                                   Authorization='Bearer test-key')
            logger.debug(
                'Message was published to %r, body: %r', topic_name, body)
        except Exception as e:
            error_msg = "Pub/Sub API is unavailable. Error: {}".format(e)
            raise Exception(error_msg)

    def create_subscription(self,
                            topic_path,
                            subscription_name):
        sub_full_name = self._get_full_subscription_name(
            subscription_name)

        try:
            self.subscriber.create_subscription(
                sub_full_name,
                topic_path)
        except AlreadyExists:
            pass

    def _get_clients(self):
        publisher = pubsub.PublisherClient()
        subscriber = pubsub.SubscriberClient()
        return publisher, subscriber

    def _get_full_topic_name(self, topic_name):
        return 'projects/{}/topics/{}'.format(
            self._project_id, topic_name)

    def _get_full_subscription_name(self, subscription_name):
        return 'projects/{}/subscriptions/sub-{}'.format(
            self._project_id, subscription_name)

    def delete_subscription(self, subscription):
        self.subscriber.delete_subscription(
            self._get_full_subscription_name(subscription))

    def subscribe(self, subscription_name, callback):
        full_name = self._get_full_subscription_name(subscription_name)
        subscription = self.subscriber.subscribe(full_name, callback)
        return subscription


def _get_pubsub_client(project_id):
    return PubSubClient(project=project_id)


def pubsub_run_test():
    print("Start Check Pubsub Emulators Connection")
    project_id = "demo"
    pubsub_client = _get_pubsub_client(project_id)
    pubsub_client._get_clients()
    print("Check Pubsub Emulators Connection OK")
