from django.urls import path
from .views import (
    ConferenceList,
    ConferenceDetails,
    ConferenceCreateView,
    ConferenceUpdateView,
    ConferenceDelete  # 👈 you forgot to import this
)

app_name = "ConferenceApp"

urlpatterns = [
    path("list/", ConferenceList.as_view(), name="list_conference"),
    path("details/<int:pk>/", ConferenceDetails.as_view(), name="ConferenceDetails"),
    path("form/", ConferenceCreateView.as_view(), name="ConferenceAdd"),
    path("<int:pk>/edit/", ConferenceUpdateView.as_view(), name="ConferenceUpdate"),
    path("<int:pk>/delete/", ConferenceDelete.as_view(), name="ConferenceDelete"),  # 👈 remove the extra “C”
]
