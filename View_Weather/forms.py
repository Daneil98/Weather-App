from django import forms

class Location(forms.Form):
    location = forms.CharField(max_length=20, label='location')
    