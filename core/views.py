from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, "main.html")
    if request.method == 'POST':
        request.POST.get('start_ip')
        return HttpResponse("response")