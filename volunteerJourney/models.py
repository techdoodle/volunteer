from django.conf import settings
from django.db import models
from django.utils import timezone
from ngoJourney.models import *


# model for volnteer registration
class volunteer(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False, unique=True)
    # password = models.CharField(max_length=15, blank=False, null=False)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followers')
    address = models.CharField(max_length=200, blank=False, null=False)
    pincode = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)

    # model returns the name of the volunteer
    def __str__(self):
        return self.name.username


# building image path and uploading it as per event basis
def get_image_path(instance, filename):
    return 'images/%s/%s' % (instance.user.user.username, filename)

# Volunteer Journey after joining the site
class journey(models.Model):
    user = models.ForeignKey(volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    group = models.ManyToManyField(volunteer, blank=True, related_name='groups')
    description = models.TextField()
    feedback = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.name.username) + ", " + str(self.event.eventName)



    
