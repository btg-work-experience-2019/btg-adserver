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


### Creating a project

1. Download Django by accessing the pip install from https://pypi.org/project/Django/

2. Create a a new project. At this point you should be in your virtual environment.
```bash
$ django-admin startproject <NAME OF SITE>
```

3. Create a development server. Make sure you're in the sites directory.
```bash
$ python manage.py runserver
```


### Syncing database structure with the code from master

1. Pull code from master using:
```bash
$ git pull <REMOTE> <BRANCH>
```

2. Merge codes together using:
```bash
 $ git merge <BRANCH>
 ```
