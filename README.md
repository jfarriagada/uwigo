# Uwigo Developer Test by Farriagada

## Virtualenv
```shell
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
```

## Project
```shell
$ git clone https://github.com/jfarriagada/uwigo.git
$ pip install -r requirements.txt
$ cd uwigo
$ python manage.py migrate
```

## Setup load initial data"
```shell
$ chmod +x loaddata.sh
$ ./loaddata.sh
```

## Login
ADMIN uwigo:farriagada <br />
USER invitado:farriagada

## PD
El usuario uwigo tiene el permiso 'add_ticket' por lo que puede crear tickets y el usuario invitado no.

