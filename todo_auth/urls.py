from django.urls import path
from .views import *

urlpatterns=[
    path('',login_,name='login_'),
    path('register_',register_,name='register_'),
    path('logout_',logout_,name='logout_'),
]