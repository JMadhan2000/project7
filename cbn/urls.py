from cbn.views import *
from django.urls import path
app_name='cbn pappu'
urlpatterns=[
    path('chandranna/',chandranna,name='chandranna'),
    path('chandranna_dialogue/',chandranna_dialogue,name='chandranna_dialogue'),
]