# Local Setup
- Clone the project
- Run `
```sh 
#run this command to spin up the local development 
$ python main.py
```

# Local Development Run
- `local_run.sh` It will start the flask app in `development`. Suited for local development



# Folder Structure

- `db_directory` has the sqlite DB. It can be anywhere on the machine. Adjust the path in ``application/config.py`. Repo ships with one required for testing.
- `application` is where our application code is
- `.gitignore` - ignore file
- 
- `main.py`  Used to run the flask application in development mode
- 
- `templates` - Default flask templates folder
used bootstrap cdn for styling purposes


```
├── application
│   ├── config.py
│   ├── controllers.py
│   ├── database.py
│   ├── __init__.py
│   ├── models.py
│   └── __pycache__
│       ├── config.cpython-36.pyc
│       ├── config.cpython-37.pyc
│       ├── controllers.cpython-36.pyc
│       ├── controllers.cpython-37.pyc
│       ├── database.cpython-36.pyc
│       ├── database.cpython-37.pyc
│       ├── __init__.cpython-36.pyc
│       ├── __init__.cpython-37.pyc
│       ├── models.cpython-36.pyc
│       └── models.cpython-37.pyc
├── db_directory
│   └── test.db
├── local_run.sh
├── local_setup.sh
├── main.py
├── templates
|   ├── addasboard.html
│   ├── 403.html
│   ├── 404.html
│   ├── userdashboard.html
│   ├── editshow.html
│   └── editvenue.html
|   ├── showad.html
│   ├── adminlogin.html
│   ├── userlogin.html
|   ├── userregister.html
│   ├── analytics.html
│   ├── housefull.html
│   └── venuead.html
|   └── booking.html
    └── mybookings.html
    └── rating.html
    └── search.html
    └── thanks.html
├── readme.md

