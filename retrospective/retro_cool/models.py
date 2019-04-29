from django.db import models

# Create your models here.


class Retrospective:

    def __init__(self, room, date, keep=[], improve=[]):
        self.room = room
        self.date = date
        self.keep = keep
        self.improve = improve

    def add_to_keep(self, item):
        self.keep.append(item)

    def add_to_improve(self, item):
        self.improve.append(item)
