# MongoDB run from docker container

MONGODB_NAME="mongo-testdb"
PORT=27017




run:
	sudo docker run -d -p $(PORT):$(PORT) --name=$(MONGODB_NAME) mongo:latest
verify-run:
	sudo docker ps 
mongo-shell-access:
	sudo docker exec --it $(MONGODB_NAME) mongo

stop-mongodb-container:
	sudo docker stop $(MONGODB_NAME)
	sudo docker rm  `sudo docker ps -a -f status=exited -q`
	sudo docker rmi `sudo docker images -q -f dangling=true`
docker-list:
	sudo docker image ls && sudo docker container ls






# SETUP DOCKER MONGODB IMAGE
pull:
	sudo docker pull mongo:latest

t:
	echo Hi < echo pierre
	