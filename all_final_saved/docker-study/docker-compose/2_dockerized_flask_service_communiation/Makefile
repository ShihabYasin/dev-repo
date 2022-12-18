BACKEND_CONTAINER_NAME=demo_backend_container
FRONTEND_CONTAINER_NAME=demo_frontend_container


BACKEND_IMAGE_NAME=demo_backend_image
FRONTEND_IMAGE_NAME=demo_frontend_image

fresh_build:
	sudo docker-compose rm -f  ; docker-compose up --build --remove-orphans ;

start:
	sudo docker-compose up --build
stop:
	sudo docker-compose down

# docker related
rmc:
	sudo docker rm -f $(BACKEND_CONTAINER_NAME)
	sudo docker rm -f $(FRONTEND_CONTAINER_NAME)

rmi:
	sudo docker rmi -f $(BACKEND_IMAGE_NAME)
	sudo docker rmi -f $(FRONTEND_IMAGE_NAME)


list:
	sudo docker image ls && sudo docker container ls
clean_all_unused:
	sudo docker rm  `sudo docker ps -a -f status=exited -q`  ;  sudo docker rmi `sudo docker images -q -f dangling=true` ;

c_dp:
	sudo docker run -p 7102:7102 --name 2_day_provider_con 2_day_provider
