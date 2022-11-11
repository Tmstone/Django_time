from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def word(request):
    return render(request, 'random_word/index.html')


def create(request):
    return redirect('random_word/index.html')


def reset(request):
    return
