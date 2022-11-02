import os

script_path = "~/StudyProjects/dev-repo"

print(f"""
      0: shut down
      1: reboot
      2: monitor reset
      3: git commit dev-repo
      
      """)

var = input("Please Enter Choice: ")
if var == "0":
    os.system("poweroff")
elif var == "1":
    os.system("reboot")
elif var == "2":
    os.system("rm -rf /etc/X11/xorg.conf")
    os.system("poweroff")
elif var == "3":
    os.system(f".{script_path}/git_commit_auto_script.sh")
else:
    print("Bye Bye !!!")
    
    
exit (0)