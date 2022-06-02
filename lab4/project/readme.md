> psql postgres

> CREATE USER anast WITH password 'password';

> CREATE DATABASE mydb OWNER anast;

> psql --user=anast mydb

> python ./manage.py showmigrations

> python ./manage.py makemigrations

> python ./manage.py dbshell

> python ./manage.py migrate
