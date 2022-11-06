project_name=project_testing__auth
app_name=new_test_app

db_name=db.sqlite3
port=8000

start_project_path=~/StudyProjects/dev-repo/Techs/Django/folder_template/saved/templates/start_project

	
start-a-new-project-with-a-new-app:
	make -k clear-dir clear-port create-project copy-debug-settings make-static-dir create-app create-super-user runserver
	# make -k clear-dir clear-port create-project 
	# make -k copy-debug-settings
	# make -k make-static-dir 
	# make -k create-app 
	# make -k create-super-user 
	# make -k runserver


copy-debug-settings:
	rm ${project_name}/settings.py
	cp ${start_project_path}/debug.settings.py ${project_name}/settings.py
	# python3 scripts/proj_init.py --options current_app_init --appname ${app_name}  --projname ${project_name}

create-super-user:
	python3 manage.py createsuperuser


## migrations study: https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
makemigrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

reinitialize-all-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm -rf ${db_name}
	make -k makemigrations create-super-user runserver

runserver:
	python3 manage.py collectstatic --noinput
	python3 manage.py check
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver 127.0.0.1:${port}

pytest:
	pytest -v --ds=${DJANGO_SETTINGS_MODULE} --capture=no  -n 2  # --reuse-db --no-migrations # -rs  # --cov # -n 2 --capture=no 
	# --reuse-db # --create-db # --migrations # -v # -k <search_string> # -m <marker> # --maxfail = <num> # --junitxml="result.xml"

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
	# touch ${app_name}/urls.py
	cp -R ${start_project_path}/scripts .  # commenting to use local changed version  not to copy from github repo

	cp ${start_project_path}/home.html ${app_name}/templates/${app_name}/home.html
	# rm ${app_name}/urls.py
	cp ${start_project_path}/urls.py ${app_name}/urls.py

	rm ${app_name}/views.py
	cp ${start_project_path}/views.py ${app_name}/views.py

	make -k add-current-app-in-settings	
		
	python3 manage.py migrate
	python3 manage.py check


add-current-app-in-settings:
	python3 scripts/proj_init.py --options current_app --appname ${app_name}  --projname ${project_name}

add-app-model-class-in-admin:
	python3 scripts/proj_init.py --options add-app-model-class-in-admin --appname ${app_name}  --projname ${project_name}

add-default-app:
	python3 scripts/proj_init.py --options reg_default_app --appname ${app_name}  --projname ${project_name}

clear-port:
	sudo kill -9 `sudo lsof -t -i:${port}`


run-etl-scripts:
	# python3 manage.py  runscript etl  -v3

clone-some-repo-with-code:
	# git clone https://github.com/encode/django-rest-framework

## For Ref Learn Here: https://github.com/brobin/django-seed
## Note: When seeding models with Foreign Keys, you need to make sure that those models are seeded first.
## For example, if a model in app A has a foreign key to a model in app B, you must seed app B first.
populate-db-with-fake-data:   
	python3 manage.py seed ${app_name} --number=15 #--seeder "MyModel.my_field" "1.1.1.1"

TODO:
	deploy case e static file handling shikha