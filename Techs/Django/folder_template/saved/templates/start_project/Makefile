project_name=custommodelfieldsproject
app_name=custommodel

port=8000


clear-dir:
	find . ! -name 'Makefile' -type f -exec rm -f {} +
	find . ! -name 'Makefile' -type d -exec rm -rf {} +

create-project:
	django-admin startproject ${project_name} .

make-static-dir:
	mkdir ${project_name}/static
	mkdir templates

create-app:
	python3 manage.py startapp ${app_name}
	mkdir ${app_name}/static
	mkdir ${app_name}/static/${app_name}
	mkdir ${app_name}/templates
	mkdir ${app_name}/templates/${app_name}
	
	touch ${app_name}/forms.py
	touch ${app_name}/urls.py
	cp -R  ~/StudyProjects/Django/DjangoTemplateFiles/saved/scripts .

	cp ~/StudyProjects/Django/DjangoTemplateFiles/saved/home.html ${app_name}/templates/${app_name}/home.html
	rm ${app_name}/urls.py
	cp ~/StudyProjects/Django/DjangoTemplateFiles/saved/urls.py ${app_name}/urls.py

	rm ${app_name}/views.py
	cp ~/StudyProjects/Django/DjangoTemplateFiles/saved/views.py ${app_name}/views.py

	python3 manage.py migrate
	python3 manage.py check

add-app:
	python3 scripts/proj_init.py --options reg_default_app --appname ${app_name}  --projname ${project_name}

create-super-user:
	python3 manage.py createsuperuser

clear-port:
	sudo kill -9 `sudo lsof -t -i:${port}`

makemigrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

runserver:
	# python3 manage.py collectstatic
	python3 manage.py check
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver 127.0.0.1:${port}

start-a-new-project-with-a-new-app:
	make -k clear-dir clear-port create-project make-static-dir create-app add-app create-super-user runserver


run-etl-scripts:
	# python3 manage.py  runscript etl  -v3

clone-some-repo-with-code:
	# git clone https://github.com/encode/django-rest-framework


TODO:
	deploy case e static file handling shikha