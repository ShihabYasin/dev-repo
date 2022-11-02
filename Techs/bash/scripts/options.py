import os

print(f"""
      0: shut down
      1: reboot
      2: monitor reset
      
      """)

var = input("Please Enter Choice: ")
if var == "0":
    os.system("poweroff")
elif var == "1":
    os.system("reboot")
else:
    print("Bye Bye !!!")
    
    
exit (0)