from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create new table for the extra info about the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
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