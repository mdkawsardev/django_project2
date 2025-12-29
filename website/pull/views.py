from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page. I'm here")
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')