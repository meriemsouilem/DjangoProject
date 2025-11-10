from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # 👈 ADD DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceModel
from django.c


# --- Vue fonctionnelle optionnelle ---
def all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, 'conferences/list_conference.html', {"list": conferences})

# --- Liste des conférences ---
class ConferenceList(ListView):
    model = Conference
    context_object_name = "list"
    ordering = ["start_date"]
    template_name = "conferences/list_conference.html"


# --- Détails d’une conférence ---
class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conferences/detail.html"
    context_object_name = "conference"


# --- Création d’une conférence ---
class ConferenceCreateView(LoginRequiredMixin,CreateView):
    model = Conference
    template_name = "conferences/conference_form.html"
  # fields = "__all__"
    success_url = reverse_lazy("ConferenceApp:ConferenceList")
    form_class = ConferenceModel

# --- Mise à jour d’une conférence ---
class ConferenceUpdateView(UpdateView):  # 👈 renommons ici pour cohérence
    model = Conference
    template_name = "conferences/conference_form.html"
  # fields = "__all__"
    success_url = reverse_lazy("ConferenceApp:ConferenceList")
    form_class=ConferenceModel
 # DeleteView
class ConferenceDelete(DeleteView):
    model = Conference
    template_name = "conferences/conference_confirm_delete.html"
    success_url = reverse_lazy("ConferenceApp:ConferenceList")