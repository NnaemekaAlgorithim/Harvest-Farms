from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def typography(request):
    return render(request, 'typography.html')
