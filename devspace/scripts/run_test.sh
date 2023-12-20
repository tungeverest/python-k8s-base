kubectl exec -it deploy/app-demo-deploy -- python devspace/create_test_pubsub.py
kubectl exec -it deploy/app-demo-deploy -- python devspace/create_test_storage.py
kubectl exec -it deploy/app-demo-deploy -- python manage.py db upgrade
kubectl exec -it deploy/app-demo-deploy -- env DEBUG=False DD_DOGSTATSD_DISABLE=1 DD_TRACE_DEBUG=0 DD_TRACE_ENABLED=0 py.test $1 --cov=dhh_images --cov-report xml
