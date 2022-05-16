from django.contrib import admin
from .models import Company, Branch, Usertype
# Register your models here.

admin.site.register([Company, Branch, Usertype])