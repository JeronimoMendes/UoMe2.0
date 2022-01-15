from django.db import models
from django.db.models.fields.related import ForeignKey


class Group(models.Model):
    relations = models.ManyToManyField("Relation")
    movements = models.ManyToManyField("Movement")

class Profile(models.Model):
    email_notifications = models.BooleanField(default=True)
    groups = models.ManyToManyField("Group")

class Movement(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField() # if < 0, user2 is borrowing from user1
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Relation(models.Model):
    user1 = models.ForeignKey(Profile, related_name="user1",on_delete=models.CASCADE)
    user2 = models.ForeignKey(Profile, related_name="user2",on_delete=models.CASCADE)
    balance = models.IntegerField(default=0) # if < 0, user2 owes money to user1
    movements = models.ManyToManyField("Movement")
