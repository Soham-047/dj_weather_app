"""
WSGI config for weather project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, django
import sys
from django.core.wsgi import get_wsgi_application

path = '/home/sohamm/dj_weather_app'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

activate_this = '/home/sohamm/.virtualenvs/myenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

django.setup()

application = get_wsgi_application()

app = application
