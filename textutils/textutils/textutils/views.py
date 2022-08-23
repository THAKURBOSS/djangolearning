# I have created this file 
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request,'index.html')


def analyze(request):
    djtext =request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    #check checkbox value
    
    #if removepunc is on then execute this 

    if removepunc == "on":
            
        # analyzed = djtext
        punctuation = '''()}[[';.'][]]['./;[,!@#$%^&*()_+'''
        analyzed = ""
        for char in djtext :
            if char not in punctuation:
                analyzed = analyzed + char
                
        params = {'purpose' : 'remove puncutation','analyzed_text':analyzed}
        return render(request, "analyze.html",params)
    
    
    #to check fullcaps is on 
    
    elif(fullcaps == 'on'):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params = {'purpose' : 'changed to upper case','analyzed_text':analyzed}
        return render(request, "analyze.html",params)
    
    
    #to remove new line 
    
    elif(newlineremover == 'on'):
        analyzed = " "
        for char in djtext:
            if char != '\n' and char != '\r':
             analyzed = analyzed + char
            
        params = {'purpose' : 'removed new line','analyzed_text':analyzed}
        return render(request, "analyze.html",params)
    
    #extra space remover
    
    elif(extraspaceremover == 'on'):
        analyzed = " "
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                
            
             analyzed = analyzed + char
            
        params = {'purpose' : 'removed new line','analyzed_text':analyzed}
        return render(request, "analyze.html",params)
    
    
    #error
    
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

