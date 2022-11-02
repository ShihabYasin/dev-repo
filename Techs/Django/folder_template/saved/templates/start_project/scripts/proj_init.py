#!/usr/bin/env python
from audioop import add
import argparse
import os
from random import randint, random
import shutil
import ast
from pathlib import Path


# CORS, if enabled here, also enable in MIDDLEWARE & IN CUSTOM-SECTION below. not for production.
# project apps

def write_in_file(file_path: str, writeit: str, atline: int, skip_no_of_lines: int) -> None:
    full_file = open(file_path, 'r').readlines()

    pre_string = full_file[:atline]
    post_string = full_file[atline + skip_no_of_lines:]
    tmp_file = f'tmp_{randint(1,100)}.py'
    for line in pre_string:
        print(line, end='', file=open(tmp_file, 'a'))
    print(writeit, end='\n', file=open(tmp_file, 'a'))
    for line in post_string:
        print(line, end='', file=open(tmp_file, 'a'))
    shutil.copyfile(tmp_file, file_path)
    os.remove(tmp_file)


def register_app_in_project(apps_to_add: list, project_name: str):
    settings_file_path = project_name + '/settings.py'
    setting_file_text = open(settings_file_path, 'r').readlines()
    start_found = False
    write_atline = -1
    for idx, line in enumerate(setting_file_text):
        if "INSTALLED_APPS = " in line:
            start_found = True
        if "]" in line and start_found:
            write_atline = idx
            # print(f"{idx}: {line}")
            break
    writeit = "\n#    added apps    \n"+"    " + \
        ',\n    '.join(f"\"{x}\"" for x in apps_to_add) + ",\n]"
    write_in_file(file_path=settings_file_path,
                  writeit=writeit, atline=write_atline, skip_no_of_lines=1)


def search_and_write_in_file(file_path: str, serach_start_str: str, serach_end_str: str, skip_no_of_lines: int, writeit: str):
    file_text = open(file_path, 'r').readlines()
    start_found = False
    write_atline = -1
    for idx, line in enumerate(file_text):
        if serach_start_str in line:
            start_found = True
        if serach_end_str in line and start_found:
            write_atline = idx
            break
    write_in_file(file_path=file_path,
                  writeit=writeit, atline=write_atline, skip_no_of_lines=skip_no_of_lines)


if __name__ == '__main__':

    parser = argparse.ArgumentParser("Give stage count.")
    parser.add_argument('-o', "--options", help="register_app", type=str)
    parser.add_argument('-a', "--appname", help="Provide app name.", type=str)
    parser.add_argument('-p', "--projname",
                        help="Provide project name.", type=str)

    args = parser.parse_args()

    default_utility_apps = [
        'livereload', 'django_extensions', 'rest_framework', 'corsheaders']
    APP_NAME = args.appname
    PROJECT_NAME = args.projname

    run_setup_stage = str(args.options)

    # if run_setup_stage == 'reg_default_app':
    #     # adding default apps 
    #     search_and_write_in_file(file_path=os.path.join(PROJECT_NAME, "settings.py"), serach_start_str="INSTALLED_APPS = [", serach_end_str="]",
    #                              skip_no_of_lines=1, writeit="\n#    added apps    \n"+"    " +
    #                              ',\n    '.join(f"\"{x}\"" for x in default_utility_apps) + ",\n]")
    #     # adding my app in project
    #     search_and_write_in_file(file_path=os.path.join(PROJECT_NAME, "settings.py"), serach_start_str="INSTALLED_APPS = [", serach_end_str="]",
    #                              skip_no_of_lines=1, writeit="\n#    added apps    \n"+"    " +
    #                              ',\n    '.join(f"\"{x}\"" for x in [APP_NAME]) + ",\n]")
    #     # adding app urls in projects urls
    #     search_and_write_in_file(file_path=os.path.join(PROJECT_NAME, "urls.py"), serach_start_str="urlpatterns = [", serach_end_str="]",
    #                              skip_no_of_lines=1, writeit=f"    path(\"\", include(\"{APP_NAME}.urls\")),\n]")
    
    
    
    if run_setup_stage == 'reg_default_app':
         # adding default apps 
        search_and_write_in_file(file_path=os.path.join(PROJECT_NAME, "settings.py"), serach_start_str="INSTALLED_APPS = [", serach_end_str="]",
                                 skip_no_of_lines=1, writeit="\n#    added apps    \n"+"    " +
                                 ',\n    '.join(f"\"{x}\"" for x in default_utility_apps) + ",\n]")
        # adding my app in project
        search_and_write_in_file(file_path=os.path.join(PROJECT_NAME, "settings.py"), serach_start_str="INSTALLED_APPS = [", serach_end_str="]",
                                 skip_no_of_lines=1, writeit="\n#    added apps    \n"+"    " +
                                 ',\n    '.join(f"\"{x}\"" for x in [APP_NAME]) + ",\n]")
        
        
         # adding include() in proj urls 
        search_and_write_in_file(file_path=os.path.join(PROJECT_NAME, "urls.py"), serach_start_str="from django.urls import path", serach_end_str="",
                                 skip_no_of_lines=0, writeit=f"from django.urls import include")
        
        
        # adding app urls in projects urls
        search_and_write_in_file(file_path=os.path.join(PROJECT_NAME, "urls.py"), serach_start_str="urlpatterns = [", serach_end_str="]",
                                 skip_no_of_lines=1, writeit=f"    path(\"\", include(\"{APP_NAME}.urls\")),\n]")
