from django.shortcuts import render
from .models import Retrospective
from .models import KeepItem
from .models import ImproveItem

# Create your views here.


def main(request):
    args = {}
    data = Retrospective.objects.all()
    args['data'] = data
    return render(request, 'retro_cool/main.html', args)


def add(request):
    return render(request, 'retro_cool/add.html')


def view(request):
    if(request.GET.get('select_retro')):
        retro_id = request.GET.get('retro')
        toKeep = KeepItem.objects.all().filter(id=retro_id)
        toImprove = ImproveItem.objects.all().filter(id=retro_id)
        args = {"data": [toKeep, toImprove]}
        # all_retro = Retrospective.objects.all()
        # retro = all_retro[retro_id]
        # args = {}
        # args['data'] = retro
        return render(request, 'retro_cool/view.html', args)
        # Name(title=name_str).save()
        # for name in Name.objects.all():
        #     print(name)
        #     context = {'names': [name_str]}.
    return render(request, 'retro_cool/view.html')
