#!/bin/bash
minikube profile list
minikube profile demo-cluster
devspace use context demo-cluster
devspace use namespace demo-namespace
minikube status
minikube start
devspace run registry-proxy
devspace dev
