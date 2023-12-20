from google.cloud import datastore
from hamcrest import equal_to, assert_that


# SECTION - Test Store emulators connections
def datastore_run_test():
    print("Start Check Datastore Emulators Connection")
    datastore_client = datastore.Client()
    # The kind for the new entity
    kind = "Task"
    # The name/ID for the new entity
    name = "sampletask1"
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)
    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task["description"] = "Buy milk"
    # Saves the entity
    datastore_client.put(task)
    print(f"Saved {task.key.name}: {task['description']}")
    assert_that(task.key.name, equal_to("sampletask1"))
    print("Done Check Datastore Emulators Connection")
