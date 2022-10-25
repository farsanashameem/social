from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def logofun(request):
    return render(request,'core_templates/logo.html')
