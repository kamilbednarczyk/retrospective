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
        print(request.body)
        retro = Retrospective.objects.get(id=table["boardId"])
        for keep_item in table["toKeep"]:
            to_save = KeepItem(retrospective=retro, text=keep_item)
            to_save.save()
        for improve_item in table["toImprove"]:
            to_save = ImproveItem(retrospective=retro, text=improve_item)
            to_save.save()
        return HttpResponseRedirect('/')

    if request.method == "GET":
        if request.GET.get('retroSubmit'):
            new_room = request.GET.get('newRoom')
            new_date = request.GET.get('newDate')

            new_id = get_new_retrospective_id(new_room, new_date)

        context = {'roomName' : new_room, 'date' : new_date, 'boardId' : new_id}

        return render(request, 'retro_cool/add.html', context)


def view(request):
    if(request.POST.get('select_retro')):
        retro_id = request.POST.get('retro')
        retro = Retrospective.objects.get(id=retro_id)
        toKeep = KeepItem.objects.all().filter(retrospective=retro)
        toImprove = ImproveItem.objects.all().filter(retrospective=retro)
        args = {"toKeep": toKeep, "toImprove": toImprove}
        return render(request, 'retro_cool/view.html', args)
    return render(request, 'retro_cool/view.html')


def get_new_retrospective_id(new_room, new_date):
    time = datetime.datetime.now()
    format_date = datetime.datetime.strptime(new_date, '%Y-%m-%d')
    new_datetime = datetime.datetime.combine(format_date, time.time())
    print(new_datetime)

    new_retrospective = Retrospective(room=new_room, date=new_datetime)

    new_retrospective.save()

    return new_retrospective.id
