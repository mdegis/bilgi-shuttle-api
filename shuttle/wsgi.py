from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'shuttle.settings'
application = Cling(get_wsgi_application())