from django.urls import path
from app1.views import *
app1_name='bala'

urlpatterns=[
    path('balu/',balu,name='balu'),
]