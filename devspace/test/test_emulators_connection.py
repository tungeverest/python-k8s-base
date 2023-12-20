from os import getenv


# SECTION Print enviroment variable:
if __name__ == '__main__':
    from datastore import datastore_run_test
    from storage import storage_run_test
    from pubsub import pubsub_run_test
    from redis_test import redis_test_connect

    print("<<<<<<<<<<<< START CHECK EMULATORS CONNECTION >>>>>>>>>>")
    print("IS_LOCAL_CLUSTER=", getenv("IS_LOCAL_CLUSTER"))
    print("PROJECT_ID=", getenv("PROJECT_ID"))
    print("GOOGLE_APPLICATION_CREDENTIALS=", getenv("GOOGLE_APPLICATION_CREDENTIALS", ""))
    print("PUBSUB_PROJECT_ID=", getenv("PUBSUB_PROJECT_ID"))
    print("PUBSUB_EMULATOR_HOST=", getenv("PUBSUB_EMULATOR_HOST"))
    print("DATASTORE_EMULATOR_HOST=", getenv("DATASTORE_EMULATOR_HOST"))
    print("STORAGE_EMULATOR_HOST=", getenv("STORAGE_EMULATOR_HOST"))
    print("DATASTORE_EMULATOR_HOST_PATH=", getenv("DATASTORE_EMULATOR_HOST_PATH"))

    datastore_run_test()
    storage_run_test()
    pubsub_run_test()
    redis_test_connect()
    print("<<<<<<<<<<<< DONE CHECK EMULATORS CONNECTION >>>>>>>>>>")
