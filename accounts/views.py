from django.shortcuts import render


# Create your views here.
def account(request):
    return render(request, 'signin.html')

def index(request):
    return render(request, 'index.html')