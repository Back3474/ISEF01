from django import forms
from .models import Kurs, Frage

class TestSelectForm(forms.Form):
    kurs = forms.ModelChoiceField(queryset=Kurs.objects.all(),required=True)
	
class ParaTestForm(forms.Form):
    arg1 = forms.CharField(max_length=50)
    arg2 = forms.CharField(max_length=50)