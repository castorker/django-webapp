from django.shortcuts import render


def welcome(request):
    return render(request, 'quibbles/welcome.html')
