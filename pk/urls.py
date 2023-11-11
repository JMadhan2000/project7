from django.urls import path
from pk.views import *
app_name='power star'
urlpatterns=[
    path('pk/',pk,name='pk'),
    path('pk_dialogue/',pk_dialogue,name='pk_dialogue'),
]