# I have created this file 
from django.http import HttpResponse


def index(request):
    return HttpResponse('''<a href=" https://www.youtube.com/">welcome to youtube.com</a>''')

def about(request):
    return HttpResponse("hello the great lucky")