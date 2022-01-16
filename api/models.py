from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Group(models.Model):
    name = models.CharField(max_length=30, default="Group")
    users = models.ManyToManyField("Profile")
    movements = models.ManyToManyField("Movement")

    def add_movement(self, amount, creator, description):
        amount /= users.count()
        movement = Movement.objects.create(amount=abs(amount), author=creator, description=description)
        for user in self.users:
            if user == creator: 
                continue
            
            # fetch relation between users
            # there must be a better way of doing this
            # TODO: filter with an "or" (user1 == user or user2 == user)
            relation = Relation.objects.filter(user1=user)
            if not relation:
                Relation.objects.filter(user2=user)

            relation.add_movement(amount, creator, movement, False)

        self.movements.add(movement)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    groups = models.ManyToManyField("Group")

class Movement(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField() # if < 0, user2 is borrowing from user1
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default="Movement")

class Relation(models.Model):
    user1 = models.ForeignKey(Profile, related_name="user1",on_delete=models.CASCADE)
    user2 = models.ForeignKey(Profile, related_name="user2",on_delete=models.CASCADE)
    balance = models.IntegerField(default=0) # if < 0, user2 owes money to user1
    movements = models.ManyToManyField("Movement")

    def add_movement(self, amount, creator, movement, divide):
        if divide: 
            amount /= 2

        if creator == user1:
            self.balance -= amount

        self.movements.add(movement)

    def has_user(self, user):
            return user1 == user or user1 == user


# When a new User object is created, a Profile is attached
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()