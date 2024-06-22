up:
	docker compose up --force-recreate --remove-orphans

build-up:
	docker compose up --force-recreate --remove-orphans --build

build-up-scale:
ifeq ($(scale),)
	docker compose up --force-recreate --build --remove-orphans --scale locust-worker=4
else
	docker compose up --force-recreate --build --remove-orphans --scale locust-worker=$(scale)
endif

.PHONY: help up build-up build-up-scale

help:
	@echo "Available targets and usage examples:"
	@echo "  up                 : Start the Docker Compose services, forcing recreation and removing orphans."
	@echo "                       Usage: make up"
	@echo ""
	@echo "  build-up           : Build and start the Docker Compose services, forcing recreation and removing orphans."
	@echo "                       Usage: make build-up"
	@echo ""
	@echo "  build-up-scale     : Build and start the Docker Compose services with scaling options for locust-worker."
	@echo "                       Usage: make build-up-scale"
	@echo "                              make build-up-scale scale=<number>  # e.g., make build-up-scale scale=4"
