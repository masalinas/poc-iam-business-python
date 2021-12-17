# Description
Poc Keycloak Business Python Django Microservice

## install DJango dependency

```shell
pip3 install django

django-admin --version
```

## install Django Rest framework dependency

```shell
pip3 install djangorestframework
```

## Create DJango Project with one App inside

This commnad create a DJango Project with one App inside with the same name
```shell
django-admin startproject PocOliveBusinessPython
```

## Run Djando Default Application

```shell
cd PocOliveBusinessPython

python3 manage.py runserver
```

## Cretae other Djando Application

```shell
python3 manage.py startapp pizza
```

## Migrate models before start
```shell
python3 manage.py makemigrations poc_olive_business_python
python3 manage.py migrate
```

## Debuf DJango
Create a launch.json from Debug VC and select Python by Dejango