# Reading 29 to Spare confusion

# Django Best Practices: Custom User Model

Setup
To start, create a new Django project from the command line. We need to do several things:

create and navigate into a dedicated directory called accounts for our code
install Django
make a new Django project called config
make a new app accounts
start the local web server
Here are the commands to run:

$ cd ~/Desktop
$ mkdir accounts && cd accounts
$ pipenv install django~=3.1.0
$ pipenv shell
(accounts) $ django-admin.py startproject config .
(accounts) $ python manage.py startapp accounts
(accounts) $ python manage.py runserver
Note that we did not run migrate to configure our database. It's important to wait until after we've created our new custom user model before doing so.


AbstractUser vs AbstractBaseUser
There are two modern ways to create a custom user model in Django: AbstractUser and AbstractBaseUser. In both cases we can subclass them to extend existing functionality however AbstractBaseUser requires much, much more work. Seriously, don't mess with it unless you really know what you're doing. And if you did, you wouldn't be reading this tutorial, would you?

So we'll use AbstractUser which actually subclasses AbstractBaseUser but provides more default configuration.

Custom User Model
Creating our initial custom user model requires four steps:

update config/settings.py
create a new CustomUser model
create new UserCreation and UserChangeForm
update the admin
In settings.py we'll add the accounts app and use the AUTH_USER_MODEL config to tell Django to use our new custom user model in place of the built-in User model. We'll call our custom user model CustomUser.

Within INSTALLED_APPS add accounts at the bottom. Then at the bottom of the entire file, add the AUTH_USER_MODEL config.

# config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts', # new
]
...
AUTH_USER_MODEL = 'accounts.CustomUser' # new
Now update accounts/models.py with a new User model which we'll call CustomUser.

# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
We need new versions of two form methods that receive heavy use working with users. Stop the local server with Control+c and create a new file in the accounts app called forms.py.

(accounts) $ touch accounts/forms.py
We'll update it with the following code to largely subclass the existing forms.

# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
Finally we update admin.py since the Admin is highly coupled to the default User model.

# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
And we're done! We can now run makemigrations and migrate for the first time to create a new database that uses the custom user model.

(accounts) $ python manage.py makemigrations accounts
(accounts) $ python manage.py migrate
Superuser
It's helpful to create a superuser that we can use to log in to the admin and test out log in/log out. On the command line type the following command and go through the prompts.

(accounts) $ python manage.py createsuperuser
Templates/Views/URLs
Our goal is a homepage with links to log in, log out, and sign up. Start by updating settings.py to use a project-level templates directory.

# config/settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [str(BASE_DIR.joinpath('templates'))], # new
        ...
    },
]
Then set the redirect links for log in and log out, which will both go to our home template. Add these two lines at the bottom of the file.

# config/settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
Create a new project-level templates folder and within it a registration folder as that's where Django will look for the log in template. We will also put our signup.html template in there.

(accounts) $ mkdir templates
(accounts) $ mkdir templates/registration
Then create four templates:

(accounts) $ touch templates/registration/login.html
(accounts) $ touch templates/registration/signup.html
(accounts) $ touch templates/base.html
(accounts) $ touch templates/home.html
Update the files as follows:

<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
</head>
<body>
  <main>
    {% block content %}
    {% endblock %}
  </main>
</body>
</html>
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
{% if user.is_authenticated %}
  Hi {{ user.username }}!
  <p><a href="{% url 'logout' %}">Log Out</a></p>
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">Log In</a> |
  <a href="{% url 'signup' %}">Sign Up</a>
{% endif %}
{% endblock %}
<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Log In{% endblock %}

{% block content %}
<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>
{% endblock %}
<!-- templates/registration/signup.html -->
{% extends 'base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
<h2>Sign Up</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Sign Up</button>
</form>
{% endblock %}
Now for our urls.py files at the project and app level.

# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
Create a urls.py file in the accounts app.

(accounts) $ touch accounts/urls.py
Then fill in the following code:

# accounts/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
Last step is our views.py file in the accounts app which will contain our signup form.

# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
Ok, phew! We're done. Let's test it out.

Start up the server with python manage.py runserver and go to the homepage at http://127.0.0.1:8000/.


## These notes were copied Exactly from https://learndjango.com/tutorials/django-custom-user-model This was done for purely documentation for later use reasons. None of these notes are original.











