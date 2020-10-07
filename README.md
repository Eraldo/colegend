!!**Update**!!: This project has moved: https://github.com/colegend

# [![coLegend](https://www.colegend.org/static/images/coLegendLogo.png)](https://www.colegend.org)

[![GitHub version](https://badge.fury.io/gh/Eraldo%2Fcolegend.svg)](http://badge.fury.io/gh/Eraldo%2Fcolegend)
[![Build Status](https://travis-ci.org/Eraldo/colegend.svg?branch=master)](https://travis-ci.org/Eraldo/colegend)
[![Coverage Status](https://img.shields.io/coveralls/Eraldo/colegend.svg)](https://coveralls.io/r/Eraldo/colegend)
[![Documentation Status](https://readthedocs.org/projects/colegend/badge/?version=latest)](https://readthedocs.org/projects/colegend/?badge=latest)

Personal Development Platform

+   Website: <https://www.colegend.org>
+   Documentation: <http://colegend.readthedocs.org>
+   GitHub: <https://github.com/Eraldo/colegend>
+   Social: <https://www.facebook.com/colegend.org>


## Donations

Paypal:
[![Paypal](https://www.paypalobjects.com/en_US/DE/i/btn/btn_donateCC_LG.gif "Paypal")](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=eraldo%40eraldo%2eorg&lc=DE&item_name=CoLegend&item_number=colegend&currency_code=EUR&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted "Paypal")

Gratipay:
[![Gratipay](http://img.shields.io/gratipay/Eraldo.svg)](https://www.gittip.com/Eraldo)


## Installation


### Local Setup

    $ git clone https://github.com/Eraldo/colegend.git
	$ cd colegend


### Virtual Environment (using `virtualenvwrapper`)

	$ mkvirtualenv --python=python3.5 colegend
	$ workon colegend
	$ pip install -r requirements/local.txt


### Database (PostgreSQL)

    $ createdb colegend
    $ python manage.py migrate


## Settings

Moved to
[settings](http://cookiecutter-django.readthedocs.org/en/latest/settings.html).

Additional settings:

    GOOGLE_ID
    GOOGLE_KEY
    FACEBOOK_ID
    FACEBOOK_KEY
    
You need to be set as variables in your virtual environment.


## Basic Commands


### Setting Up Your Users

To create a **normal user account**, just go to Sign Up and fill out the
form. Once you submit it, you'll see a "Verify Your E-mail Address"
page. Go to your console to see a simulated email verification message.
Copy the link into your browser. Now the user's email should be verified
and ready to go.

To create an **superuser account**, use this command:

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.


### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html


### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS
compilation](http://cookiecutter-django.readthedocs.org/en/latest/live-reloading-and-sass-compilation.html).


### Celery

This app comes with Celery.

This app uses redis as a celery broker.
Starting the redis server locally:
``` {.sourceCode .bash}
redis-server /usr/local/etc/redis.conf
```

To run a celery worker:

``` {.sourceCode .bash}
cd colegend
celery -A colegend.taskapp worker -l info
```

Please note: For Celery's import magic to work, it is important *where*
the celery commands are run. If you are in the same folder with
*manage.py*, you should be right.

Starting the celery scheduler
``` {.sourceCode .bash}
celery -A colegend.taskapp beat -l info -S django
```

Starting the redis monitor
``` {.sourceCode .bash}
celery -A colegend.taskapp flower

```


### Sentry

Sentry is an error logging aggregator service. You can sign up for a
free account at <http://getsentry.com> or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and
integration with the WSGI application.

You must set the DSN url in production.

It's time to write the code!!!


## Running end to end integration tests

N.B. The integration tests will not run on Windows.

To install the test runner:

    $ pip install hitch

To run the tests, enter the colegend/tests directory and run the
following commands:

    $ hitch init

Then run the stub test:

    $ hitch test scenarios/stub.test

This will download and compile python, postgres and redis and install
all python requirements so the first time it runs it may take a while.

Subsequent test runs will be much quicker.

The testing framework runs Django, Celery (if enabled), Postgres,
HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.


## Deployment

We providing tools and instructions for deploying using Docker and
Heroku.

### Heroku

[![image](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

See detailed [cookiecutter-django Heroku
documentation](http://cookiecutter-django.readthedocs.org/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.org/en/latest/deployment-with-docker.html).
