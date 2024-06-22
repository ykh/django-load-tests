up-app:
	docker compose up app --force-recreate --remove-orphans

build-up-app:
	docker compose up app --force-recreate --remove-orphans --build

.PHONY: help up-app build-up-app

help:
	@echo "Available targets and usage examples:"
	@echo ""
	@echo "  up-app             : Start the 'app' service in Docker Compose, forcing recreation and removing orphans."
	@echo "                       Usage: make up-app"
	@echo ""
	@echo "  build-up-app       : Build and start the 'app' service in Docker Compose, forcing recreation and removing orphans."
	@echo "                       Usage: make build-up-app"