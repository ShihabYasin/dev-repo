import os
from myutility import get_columns_from_text

################################################################

root = "/media/yasin/MyStudy"

print(f"""
      0: shut down
      1: reboot
      2: monitor reset
      3: git commit dev-repo
      4: Get some columns from textfile rows
      5: Start Jmeter
      6: Setup npm starter template
      
      """)

var = input("Please Enter Choice: ")
if var == "0":
    os.system("poweroff")
elif var == "1":
    os.system("reboot")
elif var == "2":
    # https://strayobject.medium.com/fix-displayport-monitor-not-waking-on-ubuntu-18-10-a1eced577f0a
    #os.system("xrandr -q | grep DP")
    os.system("rm -rf /etc/X11/xorg.conf")
    os.system("poweroff")
elif var == "3":
    os.chdir(f"""{root}/dev-repo""")
    os.system(f"""./git_commit_auto_script.sh""")
elif var == "4":    
    delimeter = input("Delimeter e.g: ',' = ")
    columns = input('Which columns(start from 1) e.g: "1,2"   = ')
    file_path = input("File Path: ")
    get_columns_from_text(file_path=file_path,delimeter=delimeter,columns=columns)
elif var == "5":
    os.system("/media/yasin/MyStudy/Saved_Downloads/Software/apache-jmeter-5.5/bin/jmeter")
elif var == "6":
    os.system(f"""npm init -y ; npm link {root}/dev-repo/Techs/NodeJS/common-setup ; npm install """)
else:
    print("Bye Bye !!!")
    
    
exit (0)

