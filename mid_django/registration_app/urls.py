from django.urls import path
from registration_app import views as v
urlpatterns = [
    path("signup/", v.SignUp, name='signup')
]