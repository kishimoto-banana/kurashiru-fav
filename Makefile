TAG := kurashiru-fav
DOCKER_CMD :=  docker-compose

build:
	${DOCKER_CMD} build

run:
	${DOCKER_CMD} up -d

logs:
	${DOCKER_CMD} logs -f