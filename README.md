# geoloaction

## First Create a virtual enviraonement 

-->mkvirtualenv geo

-->pip install django

-->python manage.py runserver

## To create a new application

-->django-admin startproject geoloaction

-->python manage.py startapp location

## Include app to the settings under [INSTALLED_APPS]

INSTALLED_APPS = [
    'location'
]

## Include app path to the project path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('location.urls')),
]

## For Location API

http://ip-api.com/json/


## For Current User IP 

https://api.ipify.org?format=json
