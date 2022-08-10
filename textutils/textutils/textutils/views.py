# I have created this file 
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request,'index.html')


def removepunc(request):
    djtext = print(request.GET.get('text','default'))
    print(djtext)
    return HttpResponse('''remove punc  <a href="http://127.0.0.1:8000">previous</a>  <a href="http://127.0.0.1:8000/capitalizefirst">next</a>  '''  )

def capitalizefirst(request):
    return HttpResponse('''capitalize first  <a href="http://127.0.0.1:8000/removepunc">previous</a>  <a href="http://127.0.0.1:8000/newlineremover">next</a> ''') 

def newlineremover(request):
    return HttpResponse('''removes newline   <a href="http://127.0.0.1:8000/capitalizefirst">previous</a>  <a href="http://127.0.0.1:8000/spaceremover">next</a>  ''')

def spaceremover(request):
    return HttpResponse('''remove spaces  <a href="http://127.0.0.1:8000/newlineremover">previous</a>  <a href="http://127.0.0.1:8000/charcount">next</a>  ''')

def charcount(request):
    return HttpResponse('''count character  <a href="http://127.0.0.1:8000/spaceremover">previous</a>   ''')

