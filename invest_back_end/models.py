from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create new table for the extra info about the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.TextField(max_length=15, blank=True)
    age = models.IntegerField(null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Update extra info about the user
def update_profile(token, username, first_name, gender, age):
    user = User.objects.get(auth_token__key=token)
    user.username = username
    user.first_name = first_name
    user.profile.gender = gender
    user.profile.age = age
    user.save()

# Table for the list of graph comparisons of the user
class GraphComp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.IntegerField()
    stock = models.CharField(max_length=5)
    description = models.CharField(max_length=30)
    color = models.IntegerField()

def save_graphcomp(token, index, stock, description, color):
    user = User.objects.get(auth_token__key=token)

    graphcomp = GraphComp(user=user, index=index, stock=stock, description=description, color=color)
    graphcomp.save()

def del_graphcomp(token, index, stock):

    if stock!='':
        graphcomp = GraphComp.objects.filter(user__auth_token__key=token, index=index, stock=stock).delete()
    else:
        graphcomp = GraphComp.objects.filter(user__auth_token__key=token, index=index).delete()

# Table for the list of stock details of the user
class StockDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.CharField(max_length=5)
    description = models.CharField(max_length=30)

def save_stockdetail(token, stock, description):
    user = User.objects.get(auth_token__key=token)

    stockdetail = StockDetail(user=user, stock=stock, description=description)
    stockdetail.save()

def del_stockdetail(token, stock):

    stockdetail = StockDetail.objects.filter(user__auth_token__key=token, stock=stock).delete()