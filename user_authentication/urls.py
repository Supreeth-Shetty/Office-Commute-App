from django.urls import path
from .views import homePageView, register, login, register_driver, register_employee

urlpatterns = [
    path("", homePageView, name="home"),
    path("authentication/register", register, name="register"),
    path("authentication/login", login, name="login"),
    path("authentication/register/employee", register_employee, name="register_employee"),
    path("authentication/register/driver", register_driver, name="register_driver"),
    
]