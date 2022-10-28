#!/bin/bash  
## git upload auto script - example script
## CLASS_PROGRAMMING 
## command line param, example for a repo:   $1 => username/username.github.io.git

PATH_REPO=ShihabYasin/dev-repo

git remote set-url origin git@github.com:$PATH_REPO

#cd $PATH_REPO
git add .

currentDate=`date +"%Y-%m-%d %T"`
git commit -m  "Repo Updated"
git pull origin master
git push origin master

exit 1
