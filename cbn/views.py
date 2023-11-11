from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chandranna(request):
    return render(request,'cbn.html')

def chandranna_dialogue(request):
    return HttpResponse('<center><h1>Andharu yela unnaru thammllu...</h1></center>')