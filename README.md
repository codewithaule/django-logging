# django-logging
django logging help traceback and find where exactly the error is.
django logging work as a seperate program you can think of it as a simple file writer, when the system runs it tracks events and record it down into console or into file called logs in this project in name it log/warning log.
Logging is important both for development and for production sites .python logging module has four main part
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

     
 
