from jagan.views import *
from django.urls import path 
app_name='jagan mamayya'
urlpatterns=[
    path('amma_vadi/',amma_vadi,name='amma_vadi'),
    path('jagananna_asara/',jagananna_asara,name='jagananna_asara'),

]