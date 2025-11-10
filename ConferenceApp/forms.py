from django import forms
from .models import Conference

class ConferenceModel(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'theme', 'description', 'location', 'start_date', 'end_date']
        labels = {
            'name': "Nom de la conférence",
            'theme': "Thématiques",
            'description': "Description",
            'location': "Location",
            'start_date': "Date de début de la conférence",
            'end_date': "Date de fin de la conférence",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Nom de la conférence"}),
            'theme': forms.TextInput(attrs={'placeholder': "Thématiques"}),
            'description': forms.Textarea(attrs={'placeholder': "Description", 'rows': 3}),
            'location': forms.TextInput(attrs={'placeholder': "Location"}),
            'start_date': forms.TextInput(
                attrs={
                    'type': 'text',  # use 'text' so placeholder is visible
                    'placeholder': "Date de début",
                    'class': 'datepicker'  # optional: for JS datepicker
                }
            ),
            'end_date': forms.TextInput(
                attrs={
                    'type': 'text',  # use 'text' so placeholder is visible
                    'placeholder': "Date de fin",
                    'class': 'datepicker'  # optional: for JS datepicker
                }
            ),
        }
