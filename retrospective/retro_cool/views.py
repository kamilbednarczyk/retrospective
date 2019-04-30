from django.shortcuts import render
from .models import Retrospective
import datetime

# Create your views here.


def main(request):
    args = {}
    data = Retrospective.objects.all()
    args['data'] = data
    print(args)
    return render(request, 'retro_cool/main.html', args)


def add(request):
    if request.GET.get('retroSubmit'):
        new_room = request.GET.get('newRoom')
        new_date = request.GET.get('newDate')

    new_id = get_new_retrospective_id(new_room, new_date)

    context = {'roomName' : new_room, 'date' : new_date, 'boardId' : new_id}

    return render(request, 'retro_cool/add.html', context)


def view(request):
    return render(request, 'retro_cool/view.html')


def get_new_retrospective_id(new_room, new_date):
    time = datetime.datetime.now()
    format_date = datetime.datetime.strptime(new_date, '%Y-%m-%d')
    new_datetime = datetime.datetime.combine(format_date, time.time())
    print(new_datetime)

    new_retrospective = Retrospective(room=new_room, date=new_datetime)

    new_retrospective.save()

    return new_retrospective.id
