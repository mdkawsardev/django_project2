from django.shortcuts import render
from django.http import HttpResponse
from pull.models import Contact
from datetime import datetime
from django.contrib import messages
context = {
    'records': Contact.objects.all()
}
def index(request):
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page. I'm here")
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your form has been sent!")
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')

