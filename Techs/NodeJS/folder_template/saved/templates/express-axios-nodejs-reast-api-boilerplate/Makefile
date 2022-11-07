install:
	npm init -y
	npm i axios express
	npm install --save-dev --save-exact  cross-env nodemon dotenv mocha
	echo fs.inotify.max_user_watches=582222 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
run:	
	npm run start:development
testing-app:	
	npm test