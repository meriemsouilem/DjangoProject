from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.
def all_conferences(req):
  conferences=Conference.objects.all()
  return render(req, 'conferences/list_conference.html', {"list":conferences})



class ConferenceList(ListView):
  model =Conference
  context_object_name="list"
  ordering =["start_date"]
  template_name="conferences/list_conference.html"

class ConferenceDetails(DetailView):
  model =Conference
  template_name="conferences/detail.html"
  context_object_name="conference"
