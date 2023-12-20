from google.cloud import storage, exceptions
from google.auth.credentials import AnonymousCredentials

client = storage.Client(
    credentials=AnonymousCredentials(),
    project='sotatek-wesang',
)

try:
    bucket = client.create_bucket(
        bucket_or_name='sotatek-wesang',
        project='sotatek-wesang',
    )
except exceptions.Conflict:
    pass
