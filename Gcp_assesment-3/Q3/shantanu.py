import base64
from gcloud import storage


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    client = storage.Client()
    bucket = client.get_bucket('shbuk1')
    blob = bucket.blob('test-file.json')
    blob.upload_from_string(pubsub_message)

