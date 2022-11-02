.PHONY: clean build run stop inspect

IMAGE_NAME = yasin/alpine-python3-flask
CONTAINER_NAME = flask-demoapp
PORT=8000

build:
	docker build -t $(IMAGE_NAME) .

release:
	docker build \
		--build-arg VCS_REF=`git rev-parse --short HEAD` \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` -t $(IMAGE_NAME) .

run:
	docker run -d --rm -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

runi:
	docker run -it -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)  /bin/bash

# access in docker localhost from outside of docker container
runh:
	#docker run -d --rm -p 8000:8000 --network host --name $(CONTAINER_NAME) $(IMAGE_NAME)
	docker run -d --rm -p 8000:8000 --network host --links host --name $(CONTAINER_NAME) $(IMAGE_NAME)
	#docker run -it -p 8000:8000 --network host --name $(CONTAINER_NAME) $(IMAGE_NAME)  /bin/bash


inspect:
	docker inspect $(CONTAINER_NAME)

shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

stop:
	docker stop $(CONTAINER_NAME)

# Stop & delete stopped container
rmc:
	docker rm -f $(CONTAINER_NAME)

# Stop & delete stopped container
rmi:
	docker rmi -f $(IMAGE_NAME)

clean:
	docker ps -a | grep '$(CONTAINER_NAME)' | awk '{print $$1}' | xargs docker rm \
	docker images | grep '$(IMAGE_NAME)' | awk '{print $$3}' | xargs docker rmi

clean_all:
	#clean all unsuccessful build image and stopped container
	docker rm $(docker ps -a -q) && \
 	docker rmi $(docker images -q -f dangling=true)

list:
	# list all docker image and container
	docker image ls && docker container ls

clear_port:
	sudo kill -9 $(sudo lsof -t -i:$(PORT))