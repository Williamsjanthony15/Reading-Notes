## Read class 34 to Spare Confusion

# Configuring Django Settings: Best Practices

Managing Django Settings: Issues
Different environments. Usually, you have several environments: local, dev, ci, qa, staging, production, etc. Each environment can have its own specific settings (for example: DEBUG = True, more verbose logging, additional apps, some mocked data, etc). You need an approach that allows you to keep all these Django setting configurations.

Sensitive data. You have SECRET_KEY in each Django project. On top of this there can be DB passwords and tokens for third-party APIs like Amazon or Twitter. This data cannot be stored in VCS.

Sharing settings between team members. You need a general approach to eliminate human error when working with the settings. For example, a developer may add a third-party app or some API integration and fail to add specific settings. On large (or even mid-size) projects, this can cause real issues.

Django settings are a Python code. This is a curse and a blessing at the same time. It gives you a lot of flexibility, but can also be a problem – instead of key-value pairs, settings.py can have a very tricky logic.

Setting Configuration: Different Approaches
There is no built-in universal way to configure Django settings without hardcoding them. But books, open-source and work projects provide a lot of recommendations and approaches on how to do it best. Let’s take a brief look at the most popular ones to examine their weaknesses and strengths.

settings_local.py
This is the oldest method. I used it when I was configuring a Django project on a production server for the first time. I saw a lot of people use it back in the day, and I still see it now.

The basic idea of this method is to extend all environment-specific settings in the settings_local.py file, which is ignored by VCS. Here’s an example:

settings.py file:

ALLOWED_HOSTS = ['example.com']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db.example.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}

...

from .settings_local import *
view rawlocal_approach_settings.py hosted with ❤ by GitHub
settings_local.py file:

ALLOWED_HOSTS = ['localhost']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'local_db',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
view rawlocal_approach_settings_local.py hosted with ❤ by GitHub
Pros:
Secrets not in VCS.
Cons:
settings_local.py is not in VCS, so you can lose some of your Django environment settings.
The Django settings file is a Python code, so settings_local.py can have some non-obvious logic.
You need to have settings_local.example (in VCS) to share the default configurations for developers.
Separate settings file for each environment
This is an extension of the previous approach. It allows you to keep all configurations in VCS and to share default settings between developers.

In this case, you make a settings package with the following file structure:

settings/
   ├── __init__.py
   ├── base.py
   ├── ci.py
   ├── local.py
   ├── staging.py
   ├── production.py
   └── qa.py
settings/local.py:

from .base import *


ALLOWED_HOSTS = ['localhost']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'local_db',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
view rawdifferent_env_approach_settings_local.py hosted with ❤ by GitHub
To run a project with a specific configuration, you need to set an additional parameter:

python manage.py runserver --settings=settings.local
view rawrun_settings_local hosted with ❤ by GitHub
Pros:
All environments are in VCS.
It’s easy to share settings between developers.
Cons:
You need to find a way to handle secret passwords and tokens.
“Inheritance” of settings can be hard to trace and maintain.
Environment variables
To solve the issue with sensitive data, you can use environment variables.
import os


SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': int(os.environ['DATABASE_PORT']),
    }
}
view rawenv_approach_settings.py hosted with ❤ by GitHub
This is the simplest example using Python os.environ and it has several issues:

You need to handle KeyError exceptions.
You need to convert types manually (see DATABASE_PORT usage).
To fix KeyError, you can write your own custom wrapper. For example:

import os

from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    try:
      	return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_value('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_value('DATABASE_NAME'),
        'HOST': get_env_value('DATABASE_HOST'),
        'PORT': int(get_env_value('DATABASE_PORT')),
    }
}
view rawenv_approach_advanced.py hosted with ❤ by GitHub
Also, you can set default values for this wrapper and add type conversion. But actually there is no need to write this wrapper, because you can use a third-party library (we’ll talk about this later).

Pros:
Configuration is separated from code.
Environment parity – you have the same code for all environments.
No inheritance in settings, and cleaner and more consistent code.
There is a theoretical grounding for using environment variables – 12 Factors.
Cons:
You need to handle sharing default config between developers.
12 Factors
12 Factors is a collection of recommendations on how to build distributed web-apps that will be easy to deploy and scale in the Cloud. It was created by Heroku, a well-known Cloud hosting provider.

As the name suggests, the collection consists of twelve parts:

Codebase
Dependencies
Config
Backing services
Build, release, run
Processes
Port binding
Concurrency
Disposability
Dev/prod parity
Logs
Admin processes
Each point describes a recommended way to implement a specific aspect of the project. Some of these points are covered by instruments like Django, Python, pip. Some are covered by design patterns or the infrastructure setup. In the context of this article, we are interested in one part: the Configuration.

Its main rule is to store configuration in the environment. Following this recommendation will give us strict separation of config from code.

You can read more on 12factor.net.

django-environ
Based on the above, we see that environment variables are the perfect place to store settings.

Now it’s time to talk about the toolkit.

Writing code using os.environ could be tricky sometimes and require additional effort to handle errors. It’s better to use django-environ instead.

Technically it’s a merge of:

envparse
honcho
dj-database-url
dj-search-url
dj-config-url
django-cache-url
This app gives a well-functioning API for reading values from environment variables or text files, handful type conversion, etc. Let’s look at some examples.

settings.py file before:

import os


SITE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db.example.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}

MEDIA_ROOT = os.path.join(SITE_ROOT, 'assets')
MEDIA_URL = 'media/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = 'static/'

SECRET_KEY = 'Some-Autogenerated-Secret-Key'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379/1',
    }
}
view rawenviron_before.py hosted with ❤ by GitHub
settings.py file after:

import environ


root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env()
environ.Env.read_env()  # reading .env file

SITE_ROOT = root()

DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': env.db('DATABASE_URL')}

public_root = root.path('public/')
MEDIA_ROOT = public_root('media')
MEDIA_URL = env.str('MEDIA_URL', default='media/')
STATIC_ROOT = public_root('static')
STATIC_URL = env.str('STATIC_URL', default='static/')

SECRET_KEY = env.str('SECRET_KEY')

CACHES = {'default': env.cache('REDIS_CACHE_URL')}
view rawenviron_after.py hosted with ❤ by GitHub
.env file:

DEBUG=True
DATABASE_URL=postgres://user:password@db.example.com:5432/production_db?sslmode=require
REDIS_CACHE_URL=redis://user:password@cache.example.com:6379/1
SECRET_KEY=Some-Autogenerated-Secret-Key
view rawenviron_env_file hosted with ❤ by GitHub
Setting Structure
Instead of splitting settings by environments, you can split them by the source: Django, third- party apps (Celery, DRF, etc.), and your custom settings.

File structure:

project/
├── apps/
├── settings/
│   ├── __init__.py
│   ├── djano.py
│   ├── project.py
│   └── third_party.py
└── manage.py
__init__.py file:

from .django import *       # All Django related settings
from .third_party import *  # Celery, Django REST Framework & other 3rd parties
from .project import *      # You custom settings
view rawstructure.py hosted with ❤ by GitHub
Each module could be done as a package, and you can split it more granularly:

project/
├── apps/
├── settings/
│   ├── project
│   │   ├── __init__.py
│   │   ├── custom_module_foo.py
│   │   ├── custom_module_bar.py
│   │   └── custom_module_xyz.py
│   ├── third_party
│   │   ├── __init__.py
│   │   ├── celery.py
│   │   ├── email.py
│   │   └── rest_framework.py
│   ├── __init__.py
│   └── djano.py
└── manage.py
Naming Conventions
Naming of variables is one of the most complex parts of development. So is naming of settings. We can’t imply on Django or third-party applications, but we can follow these simple rules for our custom (project) settings:

Give meaningful names to your settings.
Always use the prefix with the project name for your custom (project) settings.
Write descriptions for your settings in comments.
Bad example:

API_SYNC_CRONTAB = env.str('API_SYNC_CRONTAB')
view rawbad_naming.py hosted with ❤ by GitHub
Good example:

# Run job for getting new tweets.
# Accept string in crontab format. By default: every 30 minutes.
MYAWESOMEPROJECT_TWEETS_API_SYNC_CRONTAB = env.str(
    'MYAWESOMEPROJECT_TWEETS_API_SYNC_CRONTAB', default='30 * * * *'
)
view rawgood_naming.py hosted with ❤ by GitHub
Change MYAWESOMEPROJECT to you real project name.

Django Settings: Best practices
Keep settings in environment variables.
Write default values for production configuration (excluding secret keys and tokens).
Don’t hardcode sensitive settings, and don’t put them in VCS.
Split settings into groups: Django, third-party, project.
Follow naming conventions for custom (project) settings.

### Some or all notes are taken directly from https://djangostars.com/blog/configuring-django-settings-best-practices/
