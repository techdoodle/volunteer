from django.conf import settings
from django.db import models
from django.utils import timezone


# model for volnteer registration
class volunteer(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False, unique=True)
    password = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    pincode = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)

    # model returns the name of the volunteer
    def __str__(self):
        return self.name.username
