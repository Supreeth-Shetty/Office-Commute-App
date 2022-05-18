from django.contrib import admin
from .models import Company, Branch, Usertype, Users, Location
# Register your models here.

admin.site.register([Company, Branch, Usertype, Users, Location])