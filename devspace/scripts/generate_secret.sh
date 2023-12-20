#!/bin/bash

# Get variable environments file .env
POSTGRES_DB=$(grep POSTGRES_DB .env | cut -d '=' -f 2-)
POSTGRES_USER=$(grep POSTGRES_USER .env | cut -d '=' -f 2-)
POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD .env | cut -d '=' -f 2-)
REDIS_PASSWORD=$(grep REDIS_PASSWORD .env | cut -d '=' -f 2-)

rm -rf k8s_dev/config/demo-secrets.yaml
cat <<EOF > k8s_dev/config/demo-secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: demo-secrets
  namespace: demo-namespace
type: Opaque
data:
  POSTGRES_DB: $(echo -n $POSTGRES_DB | base64)
  POSTGRES_USER: $(echo -n $POSTGRES_USER | base64)
  POSTGRES_PASSWORD: $(echo -n $POSTGRES_PASSWORD | base64)
  REDIS_PASSWORD: $(echo -n $REDIS_PASSWORD | base64)
EOF

kubectl apply -f k8s_dev/config/demo-secrets.yaml
