import os, sys

apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path.append('/usr/local/lib/python2.6/dist-packages/django/')
sys.path.append('/home/dan/public_html/baseballfornerds.com/sportsstats')

os.environ['DJANGO_SETTINGS_MODULE'] = 'sportsstats.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
