# Lainausjarjestelma
HAMK-Lainausjärjestelmä-Projekti

## Getting Started
Createsuperuser for adding items to website goto /admin for adminpanel.

Book contains basic author, title and other basic information about it

Library contains contact data
Use LibraryBook for adding items in the library 


## Installing
Clone repositery
run 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

if gives error on unavailable tables run
python3 manage.py migrate --run-syncdb 

for admin capabilities
python3 manage.py createsuper 



## Built With
Django,               https://www.djangoproject.com
Django-crispy-forms   https://django-crispy-forms.readthedocs.io/en/latest/
Pillow                https://pillow.readthedocs.io/en/stable/
