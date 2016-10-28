from django.shortcuts import render, redirect, reverse
from random import random

choices = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Create your views here.
def default(request):
    return render(request,
    'randomword/default.html')

def show(request):
    return render(request,
    'randomword/word.html')

def create(request):
    if 'count' in request.session:
        request.session['count'] = request.session['count'] + 1
    else:
        request.session['count'] = 1
    if request.method == "POST":
        request.session['word'] = ""
        for i in range(0,10):
            request.session['word'] += choices[int(random() * len(choices))]
    return redirect(reverse('word_page'))
