# Kafka run from docker container

zookeeper_container="zookeeper"
kafka_container="kafka"

zookeeper_port=2181
kafka_port=9092

host=localhost


run:
	sudo docker-compose -f docker-compose.yml up -d
verify-run:
	sudo docker ps 
kafka-shell-access:
	sudo docker exec -it kafka /bin/sh

stop-kafka-containers:
	sudo docker stop $(zookeeper_container)
	sudo docker stop $(kafka_container)
	sudo docker rm  `sudo docker ps -a -f status=exited -q`
	sudo docker rmi `sudo docker images -q -f dangling=true`
docker-list:
	sudo docker image ls && sudo docker container ls
