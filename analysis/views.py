from django.shortcuts import render


def intro(request):
    return render(request, 'intro.html')

def tree(request):
    return render(request, 'tree.html')