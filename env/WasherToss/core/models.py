from django.db import models

# Create your models here.


class Seasons(models.Model):
    year = models.IntegerField(max_length=4)


class Users(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    wins = models.IntegerField()
    losses = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Games(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    winning_p1 = models.CharField(max_length=255)
    winning_p2 = models.CharField(max_length=255)
    lossing_p1 = models.CharField(max_length=255)
    lossing_p2 = models.CharField(max_length=255)
    lossing_score = models.IntegerField()
    season = models.IntegerField()
    windspeed = models.IntegerField()


class Groups(models.Model):
    player = models.CharField(max_length=255)
