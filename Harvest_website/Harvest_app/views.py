from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'static/contacts.html')

def aboutUs(request):
    return render(request, 'static/about-us.html')

def typography(request):
    return render(request, 'static/typography.html')
