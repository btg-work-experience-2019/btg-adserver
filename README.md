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


### Creating an admin user

Tutorial link:https://docs.djangoproject.com/en/2.2/intro/tutorial02/

1. To create a user who can login to the admin site, the command is:python manage.py createsuperuser

2. Then create a username, email and password for the site.

3. The URL for the site can be pulled from the terminal: http://<given IP address>/ and add admin to the end of it, to make the URL for the admin site.
