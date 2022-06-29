
from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team


# Create your views here.

#def sanjay1(request):
    #passingvalue="sanjay"
    #return render(request,"home.html",{'obj':passingvalue})
#def sanjay2(request):
    #return HttpResponse("About")
def sanjay3(request):
    database=Place.objects.all()
    database2=Team.objects.all()
    return render(request,"index.html",{'enter':database,'object':database2})
#def sanjay4(request):
    #return HttpResponse("contact")
#def sanjay5(request):
    #return render(request,"sign.html")