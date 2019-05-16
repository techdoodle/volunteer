from django.shortcuts import render
from volunteerJourney.models import *
from ngoJourney.models import *
import os


# landing page for users
def theJourney(request):
    if request.user.is_authenticated:
        reqVolunteer = volunteer.objects.get(name=request.user)
        eventList = journey.objects.filter(user=reqVolunteer)
        return render(request, 'volunJourney.html', {'reqVolunteer': reqVolunteer, 'eventList': eventList})
    else:
        reqVolunteer = False
        return render(request, 'homePage.html', {'reqVolunteer': reqVolunteer})


# def theJourney(request):
#     return render(request, 'volunJourney.html')


