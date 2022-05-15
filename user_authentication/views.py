import os
import re
from django.shortcuts import render
from django.http import HttpResponse
from logger.logger import Applogs

log = Applogs()
log.getlogger(__file__)

def homePageView(request):
    log.debug("debug logged")
    return render(request, 'index.html')