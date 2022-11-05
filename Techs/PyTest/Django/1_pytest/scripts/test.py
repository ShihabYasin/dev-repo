
#!/usr/bin/env python
import os
from scripts.edited_proj_init import search_and_write_in_file


app_name = 'new_test_app'

def get_all_class_names_from_app(app_name):
    model_file_path= f"../{app_name}/models.py"
    file_text = open(model_file_path, 'r').readlines()
    class_names = []
    for line in file_text:
        if "class " in line and "Meta" not in line:
            class_names.append(line.strip().split(
                '(')[0].replace("class ", ""))

     
    return class_names


def register_app_model_classes_in_admin(app_name=app_name):
    app_model_path = f"../{app_name}/models.py"
    app_admin_path = f"../{app_name}/admin.py"
    # os.system(f"cat {app_model_path}")
    
    all_classes = get_all_class_names_from_app(app_name=app_name)
    admin_class_names = [f"from .models import {c}\n" for c in all_classes]
    
    for c in all_classes:
        admin_class_names.append(f"""
@admin.register({c})
class {c}Admin(admin.ModelAdmin):
    pass
    # list_display = ('', '')
    # fields = ['', '']          
""")
    
    for admin_text in admin_class_names:
        search_and_write_in_file(file_path=app_admin_path , search_start_str="--append-last",
                                 skip_no_of_lines=0,
                                 writeit=admin_text)


register_app_model_classes_in_admin(app_name=app_name)


