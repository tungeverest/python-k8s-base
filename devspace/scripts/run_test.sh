#!/bin/bash

kubectl exec -it deploy/app-demo-deploy -- python devspace/create_test_pubsub.py
kubectl exec -it deploy/app-demo-deploy -- python devspace/create_test_storage.py
kubectl exec -it deploy/app-demo-deploy -- env IS_UNITTEST=1 python manage.py db upgrade
kubectl exec -it deploy/app-demo-deploy -- env IS_UNITTEST=1 py.test $1 --cov=demo-app --cov-report xml
