from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    created_date = models.DateField()
    updated_date = models.DateField()
    company_status = models.CharField(max_length=10)

    def __str__(self):
        return self.company_id

class Branch(models.Model):
    branch_id = models.CharField(max_length=20)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_address = models.TextField()
    created_date = models.DateField()
    updated_date = models.DateField()
    branch_status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.branch_id

class Usertype(models.Model):
    usertype_id = models.IntegerField()
    usertype = models.CharField(max_length=10)
    description = models.TextField()
    updated_date = models.DateField()
    admin_id = models.IntegerField()

class Users(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_phone_number = models.CharField(max_length=10)
    user_email_id = models.EmailField(blank=True,unique=True)
    user_password = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user_type_id = models.ForeignKey(Usertype, on_delete=models.CASCADE)
    created_date = models.DateField()
    updated_date = models.DateField()
    user_status = models.CharField(max_length=10)

class Location(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    location_1 = models.TextField()
    location_2 = models.TextField()
    created_date = models.DateField()
    updated_date = models.DateField()

# python manage.py makemigrations (creating migration file command)

# python manage.py sqlmigrate user_authentication 0001 (creating reqired table creation qureies)

# python manage.py migrate (to launch those quries created)

