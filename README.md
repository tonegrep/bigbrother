# bigbrother
Web application for home automation platforms

Setup guide
------

1. Configure your mysql database by installing mysql-server and mysql-client packages using your package manager. For example,
``` 
sudo apt-get install mysql-server mysql-client 
```

2. For local developing make shure your `virtualenv` [is launched](https://virtualenv.pypa.io/en/latest/userguide/), then install all requirements from requirements.txt using `pip install -r requirements.txt`

3. From venv, apply model to database
```
python manage.py makemigrations
python manage.py migrate
```

4. Run project on localhost using `python manage.py runserver`
