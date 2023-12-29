# Install Make in Ubuntu| Debain
# sudo apt install make
# make -version

setup-cluster:
	sh devspace/scripts/create_cluster.sh
	sh devspace/scripts/generate_secret.sh
	docker run -d --name=registry-proxy-demo --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"

setup-emulators:
	devspace run create-emulators

gen_secret:
	sh devspace/scripts/generate_secret.sh

proxy: # make proxy
	devspace run registry-proxy

db-update: # make db-update
	devspace run migration-db

start:
	sh dev_mode.sh

up: # make up
	devspace run-pipeline start-local

dev:
	devspace dev

deploy:
	devspace deploy

debug:
	devspace run vscode-remote


re-build: # make re-build
	devspace run-pipeline rebuild-dev

pre-commit: # make pre-commit
	pre-commit run --verbose
# commit without precommit
# git commit . -m 'message...' --no-verify

pre-commit-all: # make pre-commit-all
	pre-commit run --all-files --verbose

# "flake8 ." or "devspace run flake8" to check inside minikube
linter: # make linter
	devspace run flake8

unittest: # make unittest
	sh ./devspace/scripts/run_test.sh tests/

all: linter pre-commit unittest

# Install poetry to pre-commit on local
pre-install:
	pip install poetry && poetry install --with local

echo:
	echo "demo"
