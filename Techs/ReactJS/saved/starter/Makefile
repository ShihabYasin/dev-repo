app_name=my-react-demo-app
port=3000
create-react-app-with-ts:
	npm init -y
	npm i -D typescript webpack webpack-cli ts-loader react react-dom @types/react @types/react-dom
	npx create-react-app ${app_name}
	# COPY tsconfig.js, webpack.config.js , add "magic": "webpack" in "scripts": of package.json
	# COPY src/index.tsx, index.html . run "build-continuously" then Browse index.html in browser

build-continuously: # builds the projects continuously every 1 seconds	
	watch -n 1 npm run magic



# # OTHER UTILITY RESOURCES

# tmp_file=i.sh

# install-nodejs-and-npm-using-nvm:	
# 	touch $(tmp_file)
# 	echo "#!/bin/bash" >> $(tmp_file)
	
# 	echo "curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash " >> $(tmp_file)
# 	echo "source ~/.nvm/nvm.sh" >> $(tmp_file)
# 	echo "nvm install -g 16.17.1" >> $(tmp_file)	
# 	echo "npm install -g create-react-app" >> $(tmp_file)	
# 	echo "npm install -g webpack webpack-cli ts-loader" >> $(tmp_file)	
# 	echo "npm install -g react react-dom @types/react @types/react-dom"  >> $(tmp_file)	

# 	sudo chmod  777 $(tmp_file)
# 	./$(tmp_file)	
# 	rm $(tmp_file)

# clear-port:
# 	sudo kill -9 `sudo lsof -t -i:${port}`
