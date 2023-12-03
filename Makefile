# Makefile
### Building and running the Docker services

all: build run

build:
	docker-compose build
	docker network create --driver bridge jupyterlab-network || true
	docker network create --driver bridge api-network || true

run:
	docker-compose up -d

stop:
	docker-compose down

### Starting and stopping fast api Docker services
start-api: stop-api
	docker-compose up -d api

stop-api:
	docker-compose stop api

### Starting and stopping jupyter services
start-jupyter: stop-jupyter
	docker-compose up -d jupyterlab

stop-jupyter:
	docker-compose stop jupyterlab

### Removing the Docker services
clean:
	docker-compose down -v

# Target: Run pytest
run-tests:
	docker-compose exec api sh -c 'pytest tests' 

# Target: Run clean code script
clean-code:
	docker-compose exec api sh -c 'bash ./scripts/clean_code.sh'