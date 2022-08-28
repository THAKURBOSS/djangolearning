from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Crete your views here.
def index(request):
    return render(request,'blog/index.html')
