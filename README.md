# django-logging
django logging help traceback and find where exactly the error is.
django logging work as a seperate program you can think of it as a simple file writer, when the system runs it trace events and record it down into console or into file called logs in this project in name it log/warning log.
Logging is important both for development and for production sites.  python logging module has four main part
Django logger, django Handler, Django filter , django Formatters
in settings.py paste the code below


LOGGING = {
    'version': 1,
    # Version of logging
    'disable_existing_loggers': False,
 
    'formatters':{
        'simple':{
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
             'filename': BASE_DIR / 'warning.log',
             'formatter': 'simple'
        },
 
        'console': {
            'level':'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
 
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    },
}

and in view.py 

from django.shortcuts import render
from django.http import HttpResponse
import datetime

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    logger.info('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
    return render(request, 'index.html' )
     
    to test the code run
    python manage.py runserver 
    you will find something like this on your console
    
    
C:\Users\DELL\Desktop\django-logging\django_logging>python manage.py runserver
Watching for file changes with StatReloader
Waiting for apps ready_event.
Performing system checks...

Apps ready_event triggered. Sending autoreload_started signal.
Watching dir C:\Users\DELL\Desktop\django-logging\django_logging\core\templates with glob **/*.
Watching dir C:\Users\DELL\Desktop\django-logging\django_logging\locale with glob **/*.mo.
Watching dir C:\Users\DELL\Desktop\django-logging\django_logging\core\locale with glob **/*.mo.
System check identified no issues (0 silenced).
File C:\Users\DELL\Desktop\python\Lib\site-packages\django\utils\cache.py first seen with mtime 1632435054.2676353
File C:\Users\DELL\Desktop\python\Lib\site-packages\django\contrib\auth\hashers.py first seen with mtime 1632435041.8814454
File C:\Users\DELL\Desktop\python\Lib\site-packages\django\db\backends\sqlite3\features.py first seen with mtime 1632435053.4104104
File C:\Users\DELL\Desktop\python\Lib\site-packages\pytz\exceptions.py first seen with mtime 1632435032.7699914
File C:\Users\DELL\Desktop\python\Lib\site-packages\django\core\mail\message.py first seen with mtime 1632435052.8122766
File C:\Users\DELL\Desktop\python\Lib\site-packages\django\core\paginator.py first seen with mtime 1632435052.670004
File C:\Users\DELL\Desktop\python\Lib\site-packages\django\core\cache\utils.py first seen with mtime 1632435052.720763
File C:\Users\DELL\Desktop\python\Lib\site-packages\django\db\models\fields\proxy.py first seen with mtime 1632435053.534549

     Check out django official documentation about django logging for more
https://docs.djangoproject.com/en/dev/howto/logging/
 
