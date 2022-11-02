## CUSTOM COMMANDS : YASIN

# Docker Related: 
alias dls='sudo docker image ls ; sudo docker container ls ;'
alias sd='sudo docker '
alias drm='sudo docker system prune'
# Python
alias p='python3 '
# Ubuntu Command
alias kp='read -p "Port to Kill: "  port && sudo kill -9 $(sudo lsof -t -i:$port)'
alias ts='read -p "Enter Port for dummy  server: " port && python3 -m http.server $port'
alias g='read -p  "Search: " searchterm && google-chrome "https://www.google.com/search?q=${searchte>


# Dummy Information
alias dummy='echo -e "Dummy Data Store: \n Image: https://i.imgur.com/bFDWhkK.jpeg"'
# Print all shortcuts
alias myhelp='type sd; type dls; type drm; type p; type kp; type ts; type g; type dummy;'
## after editing run  source ~/.bashrc
