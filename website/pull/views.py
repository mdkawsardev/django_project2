from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page. I'm here")
def about(request):
    return HttpResponse("This is about page")
def contact(request):
    return HttpResponse("This is contact page")