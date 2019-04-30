from django.db import models

# Create your models here.


class Retrospective(models.Model):

    room = models.CharField(max_length = 20)
    date = models.DateField()

    def __str__(self):
        return self.room


class KeepItem(models.Model):

    retrospective = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class ImproveItem(models.Model):

    retrospective = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
