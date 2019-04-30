from django.shortcuts import render
from .models import Retrospective

# Create your views here.


def main(request):
    args = {}
    data = Retrospective.objects.all()
    args['data'] = data
    print(args)
    return render(request, 'retro_cool/main.html', args)


def add(request):
    return render(request, 'retro_cool/add.html')


def view(request):
    return render(request, 'retro_cool/view.html')
