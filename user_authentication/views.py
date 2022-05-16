import os
import re
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from logger.logger import Applogs
from .models import User


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
    if request.method == 'POST':
        id = 1 
        user_name = request.POST['User Name']
        phone = request.POST['Phone']
        email = request.POST['Email Id']
        password = request.POST['password']
        password_con = request.POST['confirm password']
        company_id = int(request.POST['company_id'])
        branch_id = int(request.POST['branch_id'])
        todays_date = date.today().strftime("%d/%m/%Y")
        print(user_name, phone, email, password, password_con, type(company_id))
        users = User(
            user_id=id, user_name=user_name, user_phone_number=phone, 
            user_email_id=email, user_password=password, company_id=1, 
            branch_id=1, user_type_id=1, created_date=todays_date, updated_date=todays_date, 
            user_status='pending')
        users.save()
        return render(request, 'index.html')
    else:
        return render(request, 'signup_employee.html')

def register_driver(request):
    log.debug("routed to register_driver page")
    return render(request, 'signup_driver.html')
    
def login(request):
    log.debug("routed to login page")
    return render(request, 'login.html')
