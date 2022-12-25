# Kafka run from docker container

zookeeper_container="zookeeper"
kafka_container="kafka"

zookeeper_port=2181
kafka_port=9092

host=localhost


up:
	sudo docker-compose -f docker-compose.yml up --build -d
	sleep 5
	google-chrome http://localhost:9000
down:
	sudo docker-compose down
verify-run:
	sudo docker ps 

