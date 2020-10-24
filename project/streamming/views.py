from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def book2(request):
    return render(request, 'book2.html')

def book3(request):
    return render(request, 'book3.html')

def book4(request):
    return render(request, 'book4.html')

def book5(request):
    return render(request, 'book5.html')

def detail(request):
    return render(request, 'detail.html')

def detail2(request):
    return render(request, 'detail2.html')

def detail3(request):
    return render(request, 'detail3.html')

def detail4(request):
    return render(request, 'detail4.html')

def detail5(request):
    return render(request, 'detail5.html')