from google.cloud import pubsub_v1 as pubsub
from google.api_core.exceptions import AlreadyExists


project_id = "sotatek-wesang"
topic_id = "test"

publisher = pubsub.PublisherClient()

try:
    publisher.create_topic(f'projects/{project_id}/topics/{topic_id}')
except AlreadyExists:
    pass
