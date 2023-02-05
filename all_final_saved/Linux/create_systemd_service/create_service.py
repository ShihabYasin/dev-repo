import os
import subprocess

################################################################
service_name = input("Enter Service Name: ")
service_file_run_command = f"/usr/bin/python3  /home/yasin/Desktop/res/test.py"
################################################################
# # Add Service configuration for machine restart below Type=simple
# Restart=always
# RestartSec=3

service_description = f'''\
[Unit]
Description=Demo {service_name} service
After=multi-user.target
[Service]
Type=simple
ExecStart={service_file_run_command}
[Install]
WantedBy=multi-user.target'''

# systemd service
service_location = f"/etc/systemd/system/{service_name}.service"


def check_service_status(service_name):
    stat = subprocess.call(["systemctl", "is-active", "--quiet", service_name])
    if (stat == 0):  # if 0 (active), print "Active"
        return True
    else:
        return False

print(f"""
     Run=> sudo python3 create_service.py
      0: Check service status
      1: Stop service
      2: Restart service
      3: Create service
      """)

var = input("Please Enter Choice: ")
if var == "0":
    os.system(f"sudo systemctl status {service_name}")
elif var == "1":
    os.system(f"sudo systemctl stop {service_name} ; sudo systemctl daemon-reload ;")
elif var == "2":
    os.system(f"sudo systemctl restart {service_name};  sudo systemctl daemon-reload  ;")
elif var == "3":
    if not check_service_status(service_name=service_name):
        print(f"Creating service: {service_name}")
        with open(service_location, "w") as f:
            f.write(service_description)
    os.system(f"sudo systemctl daemon-reload ; sudo systemctl enable {service_name}.service ; sudo systemctl start {service_name}.service ; sudo systemctl status {service_name}")
