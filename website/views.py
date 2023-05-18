from django.shortcuts import render

# Create your views here.

def index(request):
    # Return homepage
    return render(request, 'index.html')

def page1(request):
    # Return otherpage
    return render(request, 'page1.html')


def page2(request):
    # Return otherpage
    return render(request, 'page2.html')
