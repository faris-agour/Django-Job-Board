from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class City(models.Model):
    name = models.CharField(max_length=33)

    def __str__(self):
        return str(self.name)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
