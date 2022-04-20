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
     



 