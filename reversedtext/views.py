from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, "D:/python/django/reversedtext_root/templates/home.html")