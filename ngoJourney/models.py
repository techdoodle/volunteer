from django.conf import settings
from django.db import models
from django.utils import timezone


# model for ngo registrations
class ngo(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False, unique=True)
    # password = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    pincode = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name.username


# model for ngos's events
class events(models.Model):
    ngo = models.ForeignKey(ngo, blank=False, null=False, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=200, blank=False, null=False)
    eventDate = models.DateTimeField(blank=False, null=False)
    description = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=9)
    lang = models.DecimalField(max_digits=9, decimal_places=9)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.eventName




