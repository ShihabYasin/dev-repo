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
alias g='read -p  "Search: " searchterm && google-chrome "https://www.google.com/search?q=${searchterm}"' # search google 


# Dummy Information
alias dummy='echo -e "Dummy Data Store: \n Image: https://i.imgur.com/bFDWhkK.jpeg https://source.unsplash.com/random"'
# Print all shortcuts
alias myhelp='type sd; type dls; type drm; type p; type kp; type ts; type g; type dummy;'
## short-cut program
alias op='python3 /media/yasin/MyStudy/dev-repo/Techs/bash/scripts/options.py'

alias h='echo Huggingface Token:   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'
source /etc/profile.d/bash_completion.sh


# Keychain - Manage ssh keys
keychain id_rsa pbkey.pem
. ~/.keychain/`uname -n`-sh


## after editing run  source ~/.bashrc

