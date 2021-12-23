# Description
PoC Keycloak Business Python Django Microservice

## install DJango dependency

```shell
pip3 install django

django-admin --version
```

## install some dependencies

```shell
pip3 install djangorestframework
pip3 install django-cors-headers
```

## Create DJango Project with one App inside

This commnad create a DJango Project with one App inside with the same name
```shell
django-admin startproject poc_olive_business_python
```

## Run Djando Default Application

```shell
cd poc_olive_business_python

python3 manage.py runserver
```

## Cretae other Djando Application

```shell
python3 manage.py startapp <APP_NAME>
```

## Migrate models before start
```shell
python3 manage.py makemigrations poc_olive_business_python
python3 manage.py migrate
```

## Debuf DJango
Create a launch.json from Debug VC and select Python by Dejango

## Install DJango Keycloak dependencies

```shell
pip3 install django-keycloak-auth
```

Configure settings.py

```shell
MIDDLEWARE = [
    #...
    'django-keycloak-auth.middleware.KeycloakMiddleware',
    #...}    
]

KEYCLOAK_EXEMPT_URIS = []
KEYCLOAK_CONFIG = {
    'KEYCLOAK_SERVER_URL': 'http://<HOST_NAME>:8080/auth',
    'KEYCLOAK_REALM': 'TESTE',
    'KEYCLOAK_CLIENT_ID': 'client-backend',
    'KEYCLOAK_CLIENT_SECRET_KEY': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
}
```

## Install dependencies from requeriments

```shell
pip3 install -r path/requirements.txt
```