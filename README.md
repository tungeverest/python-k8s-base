# python-k8s-base

 Build FastAPI + K8s with minikube + devspace

## Prerequisite

Please check folders docs to setup.

- Installed Docker
- Installed Kubernetes Client versions >=1.27.3
- Installed Minikube
- Installed gcloud cli
- Installed poetry
- Installed devspace >=6.3.2

---

## Step 1: Setup Minikube new cluster, namespace and profile for this project

**Create secrets resource for deployments**

- Linux
  >`sh devspace/scripts/create_cluster.sh && sh devspace/scripts/generate_secret.sh`

   ** NOTE: If you update values `.env` file which values have in `k8s_dev/config/dhh-image-secrets.yaml`.
   You need to new generate success by run command: `sh devspace/scripts/generate_secret.sh`

---

## Step 2: Create registry-proxy via socat port 5000 supported for MacOS

> `devspace run registry-proxy`

> After check container name `registy-proxy-demo` is running.

## Step 3: Dev Mode

### Start build and deploy DEV MODE
  >
  > `devspace run create-emulators`

  > If show many frame data => `Ctrl+C` cancel terminal runningand run 2 times command `devspace run refix` then `Ctrl+C`

  >`devspace deploy`

### Restart DEV MODE with without build image (minikube cluster running)

  >`devspace dev` without build image

**To run fast Dev Mode when restart or power off laptop**

> Script for run Minikube and start Dev Mode automation.

- Linux

  >`sh dev_mode.sh`

---

## Run setup local for app

## Option 1: Use Docker Compose without Minikube

  >`sh compose-setup.sh`

## Option 2: Use pipenv shell without docker-compose but connect minikube

- Linux
  >`poetry shell`

  >`sh poetry install`
