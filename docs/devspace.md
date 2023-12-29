# Install Devspace.sh

```bash
# https://www.devspace.sh/docs/getting-started/installation?x0=5
# AMD64
curl -L -o devspace "https://github.com/loft-sh/devspace/releases/latest/download/devspace-linux-amd64" && sudo install -c -m 0755 devspace /usr/local/bin
devspace version

# ARM64
# curl -L -o devspace "https://github.com/loft-sh/devspace/releases/latest/download/devspace-linux-arm64" && sudo install -c -m 0755 devspace /usr/local/bin
```

## DevSpace alternatives

- Okteto: <https://github.com/okteto/okteto>
- Garden.io
- Tilt: <https://tilt.dev>

---

## To update new env for Pod when you change values

Run: `devspace reset pods`

If you need to update the file devspace.yaml => Rerun `devspace dev`

## To run Pipelines, please check and update in `devspace.yaml` file

devspace run-pipeline <pipeline_name> [flag] [args]
Example 1: `devspace run-pipeline rebuild-dev`

Example 2: `devspace run-pipeline reload-pod`

Example 1: `devspace run-pipeline purge-app`

Example 3: `devspace run-pipeline purge-volumes`

---
[!https://www.devspace.sh/docs/configuration/reference]

## Run Sync file without run `devspace dev`

  >`devspace sync`

---

## To start UI logs, terminal

  >`minikube dashboard`
  >`devspace ui`
  >`devspace logs -f`
  >`devspace enter`

Devspace list check:
  >`devspace list namespaces`
  >`devspace list contexts`
  >`devspace list vars`

Analyzes the kubernetes namespace and check for potential problems
  >`devspace analyze`
  >`devspace use context demo-cluster`
  >`devspace use namespace demo-namespace`
SSH to POD
  >`ssh app.kube-demo.devspace` or `devspace run ssh-app`
