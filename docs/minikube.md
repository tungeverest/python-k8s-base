# You can be check IP

  > IP Cluster Planel: `minikube ip`

## Remove cluster

  > `minikube status`
  > `minikube profile list && minikube profile dhh-images-cluster && minikube stop && minikube delete`
  >

## Check images

  >`docker ps -a`
  >`minikube image ls --format table`

## Switch profile

  >`minikube profile dhh-images-cluster`
  >`minikube status`

Build an image by docker in local
  >`docker build -f Dockerfile.dev --build-arg CI_USER_TOKEN=$CI_USER_TOKEN  --build-arg PROJECT_ID=<PROJECT_ID> -t <image_name>:<tag> .`

Load an image of docker to inside the minikube cluster
  >`minikube image load <image_name>:<tag>`

Build an image by minikube inside the Kubernetes:
  >`minikube image build -f Dockerfile.dev --build-arg CI_USER_TOKEN=$CI_USER_TOKEN --build-arg PROJECT_ID=<PROJECT_ID> -t <image_name>:<tag> .`

K8s UI Dashboard

> `minikube dashboard`
