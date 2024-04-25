# views.py within the pages app

from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

def about(request):
    return render(request, 'pages/about.html')

def portfolio(request):
    # You can add any necessary context data here
    return render(request, 'projects/project_index.html')

def contact(request):
    return render(request, 'pages/contact.html')
