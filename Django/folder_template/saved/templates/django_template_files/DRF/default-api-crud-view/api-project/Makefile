project_name=apiproject
app_name=api


clear-dir:
	find . ! -name 'Makefile' -type f -exec rm -f {} +
	find . ! -name 'Makefile' -type d -exec rm -rf {} +
	ln -s /home/yasin/Desktop/StudyProjects/Django/DjangoTemplateFiles/django_helper .

create-project:
	django-admin startproject ${project_name} .

make-static-dir:
	mkdir ${project_name}/static
	mkdir templates

create-app:
	python3 manage.py startapp ${app_name}
	mkdir ${app_name}/static
	mkdir ${app_name}/static/img
	mkdir ${app_name}/templates
	mkdir ${app_name}/templates/${app_name}
	touch ${app_name}/forms.py
	touch ${app_name}/urls.py
	python3 manage.py migrate
	python3 manage.py check

add-app:
	@echo "\n\n\n *** Add these apps:            'livereload', 'django_extensions', 'rest_framework','corsheaders', '${app_name}',             in ${project_name}/settings/INSTALLED_APPS list. ***\n\n\n"

create-super-user:
	python3 manage.py createsuperuser


runserver:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

start-a-new-project-with-a-new-app:
	make -k clear-dir create-project make-static-dir create-app add-app create-super-user runserver



