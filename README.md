# BTG Ad Server
A basic adserver for managing display ads

## Getting Started
### Clone the repo
Make sure you are in the right directory before you do this!

```bash
$ git clone https://github.com/vzm-work-experience-2019/btg-adserver.git
```


### Creating a virtual environment

Remember: We _never_ create virtual environments in our _project_ directory!

1. Create a virtual environment if this is a new project
```bash
$ python3 -m venv <PATH_TO_DESIRED_LOCATION>
```

2. Activate the virtual environment
```bash
$ source <PATH_TO_VIRTUAL_ENV>/bin/activate
```

### Installing dependencies and running development server

1. Download Django by accessing the pip install from https://pypi.org/project/Django/ and copy into terminal:
'''bash
pip install Django
'''

2. Create a a new project. At this point you should be in your virtual environment.
```bash
$ django-admin startproject <NAME OF SITE>
```

3. Create a development server. Make sure you're in the project root.
```bash
$ python manage.py runserver
```


### Commands to run after pulling code from master for syncing database
'''bash
$ python manage.py migrate
'''

### Creating an admin user

Tutorial link:https://docs.djangoproject.com/en/2.2/intro/tutorial02/

1. To create a user who can login to the admin site, the command is:python manage.py createsuperuser

2. Then create a username, email and password for the site.

3. The URL for the site can be pulled from the terminal: http://<given IP address>/ and add admin to the end of it, to make the URL for the admin site.

 ### In order to run a test
 
 1.create a virtual enviroment python3 -m venv ~/Desktop/workspace/test-env
 2. activate the virtual enviroment source ~/Desktop/workspace/test-env/bin/activate
 3. run the django command ./manage.py test
 



[![Build Status](https://travis-ci.org/vzm-work-experience-2019/btg-adserver.svg?branch=master)](https://travis-ci.org/vzm-work-experience-2019/btg-adserver)
