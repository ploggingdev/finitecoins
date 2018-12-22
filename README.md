# Finite Coins

Source code for https://www.finitecoins.com/

Play games in your web browser

<p align="center">
    <a href="https://www.hackerschat.net/topics/finitecoins/" alt="Chat on Hackerschat">
        <img src="https://img.shields.io/badge/chat-on%20Hackerschat-brightgreen.svg" />
    </a>
    &nbsp;&nbsp;
    <a href="https://www.hackerschat.net/topics/finitecoins/forum/" alt="Forum on Hackerschat">
        <img src="https://img.shields.io/badge/forum-on%20Hackerschat-brightgreen.svg" />
    </a>
</p>

# Setup instructions

*Note* : These instructions were tested on Ubuntu 18.04. If you are using a different OS, the installation instructions will need to be tweaked.

Update package index :

```
sudo apt-get update
```

Install required packages :

```
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib redis nginx
```

Setup postgres :

```
sudo -u postgres psql

CREATE DATABASE finitecoins;

CREATE USER finitecoinsuser WITH PASSWORD 'DB_PASSWORD';

ALTER ROLE finitecoinsuser SET client_encoding TO 'utf8';

ALTER ROLE finitecoinsuser SET default_transaction_isolation TO 'read committed';

ALTER ROLE finitecoinsuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE finitecoins TO finitecoinsuser;

ALTER USER finitecoinsuser WITH SUPERUSER;

\q
```

Setup the finitecoins project :

```
git clone https://github.com/ploggingdev/finitecoins.git

sudo apt install python3-venv

cd finitecoins

mkdir venv

python3 -m venv venv/finitecoins

source venv/finitecoins/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
```

Set env variables in ~/.bashrc :

```
sudo nano ~/.bashrc
```

The following env variables are required :

```
export finitecoins_secret_key="CHOOSE_LONG_SECRET_KEY";
export finitecoins_db_name="finitecoins"
export finitecoins_db_user="finitecoinsuser"
export finitecoins_db_password="DB_PASSWORD"
export finitecoins_db_url="localhost"
export redis_url="redis://localhost:6379"
export finitecoins_postmark_token="LEAVE_BLANK"
export DJANGO_SETTINGS_MODULE=finitecoins.settings
export finitecoins_recaptcha_secret_key="RECAPTCHA_KEY"
```

Continue setup :

```
deactivate

source ~/.bashrc

source venv/finitecoins/bin/activate

python manage.py migrate
```

Create admin user :

```
python manage.py createsuperuser
```

Navigate to `http://127.0.0.1:8000/admin/` and add the following :

* "userprofile" for the admin user

*Important steps*

This project has a few external dependencies such as postmark for email and google recaptcha to reduce spam. Your local setup will need a few changes to get it to work :

1. Use a dummy email backend so that emails won't actually be sent. Change the `EMAIL_BACKEND` in `settings.py` as follows :

```
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
```

2. Recaptcha V2 is used for login and other pages such as registration, password reset. You will need to create an api key on the recaptcha site and update the following :

* In `~/.bashrc` update `finitecoins_recaptcha_secret_key`

* In `user_auth/templates/registration/login.html` update `datasite-key`

Start python and celery :

```
python manage.py runserver

celery -A finitecoins worker -B -l info
```

Visit the development server at `127.0.0.1:8000` to test the site.

If you face any issues, please visit the [finitecoins topic](https://www.hackerschat.net/topics/finitecoins/).