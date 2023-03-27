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
      6: Docker Option
      7: Run Kafka & Kafdrop GUI
      8: Run COCO Annotator
      9: Run MySql + PhPMyAdmin
      
      """)

var = input("Please Enter Choice: ")
if var == "0":
    os.system("poweroff")
elif var == "1":
    os.system("reboot")
elif var == "2":
    # https://strayobject.medium.com/fix-displayport-monitor-not-waking-on-ubuntu-18-10-a1eced577f0a
    #os.system("xrandr -q | grep DP")
    # enable BIOS Vt-d capability (Press DEL button on startup)
    # give this command to check driver "sudo lspci" and "sudo lshw -c video" . This solves the problem once.

    os.system("rm -rf /etc/X11/xorg.conf")
    os.system("poweroff")
elif var == "3":
    os.chdir(f"""{root}/dev-repo""")
    os.system(f"""./git_commit_auto_script.sh""")
elif var == "4":
    delimeter = input("Delimeter e.g: ',' = ")
    columns = input('Which columns(start from 1) e.g: "1,2"   = ')
    file_path = input("File Name (from current dir) : ")
    file_path = os.path.join( os.getcwd(),file_path)
    get_columns_from_text(file_path=file_path,
                          delimeter=delimeter, columns=columns)
elif var == "5":
    os.system(
        "/media/yasin/MyStudy/Saved_Downloads/Software/apache-jmeter-5.5/bin/jmeter")
elif var == "6":
    os.system(f"""Docker Options:\n""")
    print(f"""
      0: Show Docker List
      1: Clean all unused Docker stuffs
      2: docker compose up
      3: docker compose down
      4: stop_all_docker_container
      5: remove_all_docker_container
      6: give image name/id to remove
      """)

    var_docker = input("Docker Action: ")
    if var_docker == "0":
        os.system("sudo docker image ls ; sudo docker container ls ;")
    elif var_docker == "1":
        os.system("	sudo docker rm  `sudo docker ps -a -f status=exited -q` ; sudo docker rmi `sudo docker images -q -f dangling=true` ;")
    elif var_docker == "2":
        os.system("sudo docker-compose up")
    elif var_docker == "3":
        os.system("sudo docker-compose down")
    elif var_docker == "4":
        os.system("sudo docker kill `sudo docker ps -q`")
    elif var_docker == "5":
        os.system("sudo docker rm `sudo docker ps -q`")
    elif var_docker == "6":
        os.system("read -p 'Docker Images to remove: ' -r imls && sudo docker rmi -f  $imls")
    
    else:
        print("done ...")
elif var == "7":
    print(f"""
          0: Kafka UP
          1: Kafka DOWN
          """)
    var_docker = input("Kafka Action: ")
    if var_docker == "0":
        os.system(
            f'''cd "{root}/dev-repo/all_final_saved/Run_AS_Docker/Kafka/RUN_USING_GUI_CLIENT/Kafdrop"; make -f Makefile up''')
    elif var_docker == "1":
        os.system(
            f'''cd "{root}/dev-repo/all_final_saved/Run_AS_Docker/Kafka/RUN_USING_GUI_CLIENT/Kafdrop"; make -f Makefile down''')
elif var == "8":
    print(f"""
              0: COCO UP
              1: COCO DOWN
              """)
    var_coco = input("COCO Action: ")
    if var_coco == "0":
        os.system(f'''cd {root}/Saved_Downloads/Software/coco-annotator ;  make -f Makefile up''')
    elif var_coco == "1":
        os.system(f'''cd {root}/Saved_Downloads/Software/coco-annotator ;  make -f Makefile down''')
elif var == "9":
    print(f"""
              0: MySQL + PhPMyAdmin UP
              1: MySQL + PhPMyAdmin DOWN
              """)
    var_mysql = input("COCO Action: ")
    if var_mysql == "0":
        os.system(f'''cd {root}/dev-repo/all_final_saved/Run_AS_Docker/mysql ;  make -f Makefile up''')
    elif var_mysql == "1":
        os.system(f'''cd {root}/dev-repo/all_final_saved/Run_AS_Docker/mysql ;  make -f Makefile down''')






else:
    print("Bye Bye !!!")

exit(0)


