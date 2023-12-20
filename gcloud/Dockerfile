# https://github.com/GoogleCloudPlatform/cloud-sdk-docker/tree/master
FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest
# Open source: https://github.com/oittaa/gcp-storage-emulator
RUN pip install --no-cache-dir gcp-storage-emulator

ARG PROJECT_ID sotatek-wesang
ENV ENV local
ENV CLOUDSDK_CORE_PROJECT $PROJECT_ID
ENV GOOGLE_CLOUD_PROJECT $PROJECT_ID
ENV PUBSUB_PROJECT_ID $PROJECT_ID
ENV STORAGE_DIR storage

ENV DATASTORE_DATASET $PROJECT_ID
ENV DATASTORE_PROJECT_ID $PROJECT_ID
ENV DATASTORE_EMULATOR_HOST_PATH 0.0.0.0:6067/datastore

WORKDIR /emulators
RUN gcloud config set project $PROJECT_ID
RUN gcloud version
