from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Crete your views here.
def index(request):
    return render(request,'shop/index.html')


def about(request):
    return HttpResponse('we are at about') 

def contactus(request):
    return HttpResponse('we are at contactus')

def tracker(request):
    return HttpResponse('we are at tracker')

def search(request):
    return HttpResponse('we are at search')

def productview(request):
    return HttpResponse('we are at productview')

def checkout(request):
    return HttpResponse('we are at checkout')