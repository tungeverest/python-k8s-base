# -------------   Check List Command   ----------------

  >`kubectl cluster-info`
  >`kubectl get svc,pods -o wide`
  >`kubectl get namespaces`
  >`kubectl config get-contexts`
  >`kubectl config use-context demo-cluster`
  >`kubectl config set-context --current --namespace=demo-namespace`

Forward port to test on Kubernetes
  >`kubectl port-forward <pod-name> 8080:8000 -n demo-namespace`
  >`devspace list ports`
