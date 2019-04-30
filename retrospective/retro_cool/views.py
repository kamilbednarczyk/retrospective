from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Retrospective, KeepItem, ImproveItem
import json
import datetime

# Create your views here.


def main(request):
    args = {}
    data = Retrospective.objects.all()
    args['data'] = data
    return render(request, 'retro_cool/main.html', args)


def add(request):
    if request.method == "POST":

        table = json.loads(request.body.decode('utf-8'))
        for keep_item in table["toKeep"]:
            to_save = KeepItem(retrospective=table["boardId"], text=keep_item)
            to_save.save()
        for improve_item in table["toImprove"]:
            to_save = ImproveItem(retrospective=table["boardId"], text=improve_item)
            to_save.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'retro_cool/add.html')

    if request.GET.get('retroSubmit'):
        new_room = request.GET.get('newRoom')
        new_date = request.GET.get('newDate')

    new_id = get_new_retrospective_id(new_room, new_date)

    context = {'roomName' : new_room, 'date' : new_date, 'boardId' : new_id}

    return render(request, 'retro_cool/add.html', context)


def view(request):
    if(request.GET.get('select_retro')):
        retro_id = request.GET.get('retro')
        toKeep = KeepItem.objects.all().filter(retrospective_id=retro_id)
        toImprove = ImproveItem.objects.all().filter(retrospective_id=retro_id)
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


def get_new_retrospective_id(new_room, new_date):
    time = datetime.datetime.now()
    format_date = datetime.datetime.strptime(new_date, '%Y-%m-%d')
    new_datetime = datetime.datetime.combine(format_date, time.time())
    print(new_datetime)

    new_retrospective = Retrospective(room=new_room, date=new_datetime)

    new_retrospective.save()

    return new_retrospective.id
