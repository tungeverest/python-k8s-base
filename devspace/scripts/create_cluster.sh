#!/bin/bash

kubectl version --short
minikube profile list
devspace version

minikube start --driver=docker --container-runtime=containerd --profile demo-cluster \
        --namespace=demo-namespace --cpus 3 --memory 4096 --disk-size 20g \
        --network-plugin=cni --cni=calico  --kubernetes-version=v1.27.3

minikube profile list
minikube profile demo-cluster
minikube status
minikube addons enable registry
minikube addons list

kubectl create ns demo-namespace && kubectl get namespaces
devspace use context demo-cluster
devspace use namespace demo-namespace

cp .env.example .env

echo "LOCAL_CLUSTER_IP=$(minikube ip)" >> .env
echo "LOCAL_CLUSTER_IP=$(minikube ip) is imported in .env"

echo "PUBSUB_EMULATOR_HOST=$(minikube ip):30066" >> .env
echo "PUBSUB_EMULATOR_HOST=$(minikube ip):30066 is imported in .env"

echo "DATASTORE_EMULATOR_HOST=$(minikube ip):30067" >> .env
echo "DATASTORE_EMULATOR_HOST=$(minikube ip):30067 is imported in .env"

echo "STORAGE_EMULATOR_HOST=$(minikube ip):30023" >> .env
echo "STORAGE_EMULATOR_HOST=$(minikube ip):30023 is imported in .env"

echo "DATASTORE_EMULATOR_HOST_PATH=$(minikube ip):30067/datastore" >> .env
echo "DATASTORE_EMULATOR_HOST_PATH=$(minikube ip):30067/datastore is imported in .env"

echo "=>>>>>>>>>>>>>>>>--Create Done Minikube Cluster:
-- demo-cluster, -cpus 3 --memory 4096 --disk-size 20g
-- cni=calico --namespace=demo-namespace --kubernetes-version=v1.27.3
------------------  -----------CREATE CLUSTER DONE  --<<<<<<<<<<<<<<<<<="
