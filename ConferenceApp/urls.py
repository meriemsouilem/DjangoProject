from django.urls import path
from .views import all_conferences, ConferenceList, ConferenceDetails

app_name = "ConferenceApp"

urlpatterns = [
    #path("list/", all_conferences, name="list_conference"),
    path("list/",ConferenceList.as_view(),name="ConferenceList"),
    path("details/<int:pk>/",ConferenceDetails.as_view(),name="ConferenceDetails"),
]
