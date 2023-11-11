from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def amma_vadi(request):
    return render(request,'jagan.html')

def jagananna_asara(request):
    return HttpResponse('<center><h1><marquee>Kulam chudan mathan chudam rajakiyalu chudam rajakiyalu vheyyam..</marquee></h1></center>')