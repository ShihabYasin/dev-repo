.PHONY: clean build run stop inspect

IMAGE_NAME = yasin/alpine-python3-flask
CONTAINER_NAME = flask-demoapp
PORT=8000

build:
	sudo docker build -t $(IMAGE_NAME) .

release:
	sudo docker build \
		--build-arg VCS_REF=`git rev-parse --short HEAD` \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` -t $(IMAGE_NAME) .

run:
	sudo docker run -d --rm -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

runi:
	sudo docker run -it -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)  /bin/bash

# access in docker localhost from outside of docker container
runh:
	#docker run -d --rm -p 8000:8000 --network host --name $(CONTAINER_NAME) $(IMAGE_NAME)
	sudo docker run -d --rm -p 8000:8000 --network host --links host --name $(CONTAINER_NAME) $(IMAGE_NAME)
	#docker run -it -p 8000:8000 --network host --name $(CONTAINER_NAME) $(IMAGE_NAME)  /bin/bash


inspect:
	sudo docker inspect $(CONTAINER_NAME)

shell:
	sudo docker exec -it $(CONTAINER_NAME) /bin/bash

stop:
	sudo docker stop $(CONTAINER_NAME)

# Stop & delete stopped container
rmc:
	sudo docker rm -f $(CONTAINER_NAME)

# Stop & delete stopped container
rmi:
	sudo docker rmi -f $(IMAGE_NAME)

clean:
	sudo docker ps -a | grep '$(CONTAINER_NAME)' | awk '{print $$1}' | xargs docker rm \
	sudo docker images | grep '$(IMAGE_NAME)' | awk '{print $$3}' | xargs docker rmi

clean_all:
	#clean all unsuccessful build image and stopped container
	sudo docker rm  `sudo docker ps -a -f status=exited -q`
 	sudo docker rmi `sudo docker images -q -f dangling=true`

list:
	# list all docker image and container
	sudo docker image ls && sudo docker container ls

clear_port:
	sudo kill -9 $(sudo lsof -t -i:$(PORT))