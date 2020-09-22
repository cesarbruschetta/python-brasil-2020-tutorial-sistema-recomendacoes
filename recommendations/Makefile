.PHONY: .

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

dependencias: ## instalar dependencias
	@poetry install

black:
	poetry run black ./

run-server:
	@poetry run python ./recommendations/server.py
