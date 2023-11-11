from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pk(request):
    return render(request,'pk.html')

def pk_dialogue(request):
    return HttpResponse('<center><h1>Thala kayalu puchakayalla lechi pothai</h1></center>')