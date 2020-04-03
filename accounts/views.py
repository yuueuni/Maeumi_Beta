from django.shortcuts import render


# Create your views here.
def account(request):
    return render(request, 'new_signin.html')

def index(request):
    return render(request, 'index.html')