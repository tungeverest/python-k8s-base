# Install Make in Ubuntu| Debain
# sudo apt install make
# make -version

# commit without precommit
# git commit . -m 'message...' --no-verify
pre-commit: # make pre-commit
	pre-commit run --verbose
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

db-update: # make db-update
    devspace run migration-db

start: # make start
    devspace run-pipeline start-local

start-all:
    devspace dev

proxy: # make proxy
    devspace run registry-proxy

re-build: # make re-build
    devspace run-pipeline rebuild-dev
