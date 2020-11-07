DOCKER_NAME=python-brasil-2020-tutorial-sistema-recomendacoes_mongo_1
DOCKER_NETWORK=$(shell docker inspect -f '{{.HostConfig.NetworkMode}}' ${DOCKER_NAME})
DOCKER_IP=$(shell docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ${DOCKER_NAME})

.PHONY: .

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

docker-up: ## Inicia todos os serviçoes
	@docker-compose up -d

import-products: ## Importas os produtos no mongoDB
	@docker run -t --rm \
		--network ${DOCKER_NETWORK} \
    	--volume $(shell pwd)/ecommerce/_data:/data \
    	mongo \
		mongoimport --host ${DOCKER_IP} \
		--username pythonbrasil \
		--password pythonbrasil \
		--authenticationDatabase admin \
		--db pythonbrasil \
		--collection products \
		--jsonArray \
		/data/products.json
