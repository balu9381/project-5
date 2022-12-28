from django.urls import path
from app2.views import *
app2_name='bala'

urlpatterns=[
    path('bala/',bala,name='bala'),
]