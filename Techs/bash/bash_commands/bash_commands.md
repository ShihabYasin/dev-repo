## Here Some Useful Bash Commands:

1. How to get the 3rd column from command output? e.g:  
```sudo docker image ls | while read c1 c2 c3 c4 c5; do echo $c3; done```

2. Find named file matching from sub-dirs
```find . -name "*.txt"```

3. How to remove folders with a certain name e.g: __pycache__ 
find . -type d -name __pycache__ -delete

4. Get all file sized in current directory
```du -ch *``` or
```ls -laSh``` or ```ls -laShr```  (order changed)
```ls -laShR``` (sub-folder too)

