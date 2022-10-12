from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    try:
        characters = list()

        if request.POST.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if request.POST.get('lowercase'):
            characters.extend(list('abcefghijklmnopqrstuvwxyz'))

        if request.POST.get('special'):
            characters.extend(list('~!@#$%^&*()_+="\/|?><.:;'))

        if request.POST.get('numbers'):
            characters.extend(list('0123456789'))

        length = int(request.POST.get('length', 14))

        thepassword = ''

        for x in range(length):
            thepassword += random.choice(characters)
    except:
        thepassword = 'ERROR: Select an option to generate password'


    return render(request, 'generator/password.html', {'password': thepassword})

# Use templates to display html pages instead
