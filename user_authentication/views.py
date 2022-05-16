import os
import re
from django.shortcuts import render
from django.http import HttpResponse
from logger.logger import Applogs

log = Applogs()
log.getlogger(__file__)

def homePageView(request):
    log.debug("landed on index page")
    return render(request, 'index.html')

def register(request):
    log.debug("routed to signup page")
    return render(request, 'register.html')

def register_employee(request):
    log.debug("routed to register_employee page")
    return render(request, 'signup_employee.html')

def register_driver(request):
    log.debug("routed to register_driver page")
    return render(request, 'signup_driver.html')
    
def login(request):
    log.debug("routed to login page")
    return render(request, 'login.html')
