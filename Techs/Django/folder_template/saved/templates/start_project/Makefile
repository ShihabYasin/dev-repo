project_name=locallibrary
app_name=catalog

port=8000

start_project_path=~/StudyProjects/dev-repo/Techs/Django/folder_template/saved/templates/start_project


start-a-new-project-with-a-new-app:
	make -k clear-dir clear-port create-project make-static-dir create-app add-app create-super-user runserver
	

create-super-user:
	python3 manage.py createsuperuser

makemigrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

runserver:
	# python3 manage.py collectstatic
	python3 manage.py check
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver 127.0.0.1:${port}

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
	cp -R ${start_project_path}/scripts .

	cp ${start_project_path}/home.html ${app_name}/templates/${app_name}/home.html
	rm ${app_name}/urls.py
	cp ${start_project_path}/urls.py ${app_name}/urls.py

	rm ${app_name}/views.py
	cp ${start_project_path}/views.py ${app_name}/views.py

	python3 manage.py migrate
	python3 manage.py check

add-app:
	python3 scripts/proj_init.py --options reg_default_app --appname ${app_name}  --projname ${project_name}

clear-port:
	sudo kill -9 `sudo lsof -t -i:${port}`


run-etl-scripts:
	# python3 manage.py  runscript etl  -v3

clone-some-repo-with-code:
	# git clone https://github.com/encode/django-rest-framework


TODO:
	deploy case e static file handling shikha