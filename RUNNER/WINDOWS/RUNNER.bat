py -m venv .venv
call .venv\Scripts\activate


py -m pip install -r requirements.txt


py manage.py makemigrations
py manage.py migrate

py manage.py runserver