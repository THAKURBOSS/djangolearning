# I have created this file 
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request,'index.html')


def analyze(request):
    djtext =request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(djtext)
    print(removepunc)
    if removepunc == "on":
            
        # analyzed = djtext
        punctuation = '''()}[[';.'][]]['./;[,!@#$%^&*()_+'''
        analyzed = ""
        for char in djtext :
            if char not in punctuation:
                analyzed = analyzed + char
                
        params = {'purpose' : 'remove puncutation','analyzed_text':analyzed}
        return render(request, "analyze.html",params)
    else:
        return HttpResponse('error')
# def capitalizefirst(request):
#     return HttpResponse('''capitalize first  <a href="http://127.0.0.1:8000/removepunc">previous</a>  <a href="http://127.0.0.1:8000/newlineremover">next</a> ''') 

# def newlineremover(request):
#     return HttpResponse('''removes newline   <a href="http://127.0.0.1:8000/capitalizefirst">previous</a>  <a href="http://127.0.0.1:8000/spaceremover">next</a>  ''')

# def spaceremover(request):
#     return HttpResponse('''remove spaces  <a href="http://127.0.0.1:8000/newlineremover">previous</a>  <a href="http://127.0.0.1:8000/charcount">next</a>  ''')

# def charcount(request):
#     return HttpResponse('''count character  <a href="http://127.0.0.1:8000/spaceremover">previous</a>   ''')

