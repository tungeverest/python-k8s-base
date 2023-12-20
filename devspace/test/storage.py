import os

from google.cloud import storage
from google.auth.credentials import AnonymousCredentials
from hamcrest import (
    equal_to, assert_that, greater_than_or_equal_to, contains_string
)


# SECTION - Test Store emulators connections
def storage_run_test():
    print("Start Check Storage Emulators Connection")
    _DEFAULT_STORAGE_HOST = u"https://storage.googleapis.com"
    STORAGE_EMULATOR_HOST = os.environ.get(
        "STORAGE_EMULATOR_HOST", _DEFAULT_STORAGE_HOST)
    is_cluster = os.environ.get("IS_LOCAL_CLUSTER")
    ip_cluster = os.environ.get("LOCAL_CLUSTER_IP")
    print("STORAGE_EMULATOR_HOST=", STORAGE_EMULATOR_HOST)

    if is_cluster:
        assert_that(STORAGE_EMULATOR_HOST, equal_to("http://storage-svc:9023"))
    else:
        assert_that(STORAGE_EMULATOR_HOST, equal_to(
            "http://{}:30023".format(ip_cluster)))

    BUCKET = os.environ.get("PROJECT_ID")
    is_storage_connect = True

    try:
        client = storage.Client(
            credentials=AnonymousCredentials(),
            project=os.environ.get("PROJECT_ID"),
        )
    except Exception as e:
        is_storage_connect = False
        print("Store connection error:", e)

    assert_that(is_storage_connect, equal_to(True))
    try:
        if not client.bucket(BUCKET).exists():
            bucket = client.create_bucket(BUCKET)
        else:
            bucket = client.bucket(BUCKET)
    except Exception as e:
        is_storage_connect = False
        print("Bucket not found error:", e)

    list_bucket = [*client.list_buckets(project=os.environ.get("PROJECT_ID"))]
    print("Bucket List:", list_bucket)
    assert_that(len(list_bucket), greater_than_or_equal_to(1))
    print("Bucket Name:", bucket.name)
    assert_that(bucket.name, contains_string(BUCKET))
    print("Check Storage Emulators Connection OK")
