import os
import sys

path = '/home/ubuntu/projects'
if path not in sys.path:
    sys.path.append(path)
path = '/home/ubuntu/projects/mimir'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mimir.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
