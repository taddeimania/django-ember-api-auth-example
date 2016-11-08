# Django API w/ Ember Frontend

### What is this?

`django-ember-api-auth-example` is a project I created to provide a functioning starting point to anyone interested in starting a "Full Stack" web application that contains an Ember Single Page app on the frontend that communicates with a Django API on the backend.

This example application should work "out of the box" and provide a "Secrets" backend model / view that can only be accessed via a token authenticated request, and CRUD functionality on the frontend for your "Secrets" model.

### Why?

Starting a project with an API backend and a Single Page App frontend can take quite a bit of technology and configuration to get started and unfortunately any spark of inspiration for your app can be extinguished quickly with mountains of boilerplate code just to get started.  This repository not only acts as a starting point for my own applications but as a learning tool / starting point for others as well.  


## Technology

Frontend:

 - [Ember JS](http://emberjs.com/)
 - [ember simple auth](https://github.com/simplabs/ember-simple-auth)
 - [ember simple auth token](https://github.com/jpadilla/ember-simple-auth-token)
 - [ember django adapter](https://github.com/dustinfarris/ember-django-adapter)

Backend:
 - [Django](https://www.djangoproject.com/)
 - [Django Rest Framework](http://www.django-rest-framework.org/)
 
## Instructions

#### Setting up the backend

 - Create a `virtualenv` and install the backend dependencies by typing `pip install -r requirements.txt`
 - Migrate your database so your tables are created (will use sqlite3 by default) `python manage.py migrate`
 - Create a superuser so you can log into your application. `python manage.py createsuperuser`
 - Run your server `python manage.py runserver`

Now you're ready to open a new terminal tab or however you want to start a new process.

#### Setting up the frontend

 - Change the current directory to `example_app/static/example_app/`
 - Install your frontend dependencies by running the command `npm install`. This can take a while.
 - Install your bower dependencies by running the command `bower install`. This should not take a while.
 - Run your frontend watch server to built your `dist` directory by running the command `ember serve`

Once it finishes it's initial build of your application you can navigate your browser to `http://localhost:8000` and login with your superuser credentials.

You should now be able to create a few secrets in the UI.

From here you can begin adding to your application! Have fun!
