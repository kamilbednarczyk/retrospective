from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'retro_cool/main.html')


def add(request):
    return render(request, 'retro_cool/add.html')


def view(request):
    return render(request, 'retro_cool/view.html')
