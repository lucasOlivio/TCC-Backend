from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

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
def update_profile(request, user_id, gender, age):
    user = User.objects.get(pk=user_id)
    user.profile.gender = gender
    user.profile.age = age
    user.save()