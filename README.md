## Getting started
This project use pipenv. Install via pip:
```
$ pip install pipenv
```

Create a `.env` and set SECRET_KEY. Install the dependencies, migrate the database, and run the server.

```shell
# Install the dependencies
pipenv install
# Run the database migrations
python manage.py migrate
# Start the server
python manage.py runserver
```

Python 3.11.1