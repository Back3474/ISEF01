from django import forms
from .models import Kurs

COUNT_CHOICE= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20')
    ]

class TestSelectForm(forms.Form):
    kurs = forms.ModelChoiceField(queryset=Kurs.objects.all(),required=True)
    questioncount = forms.IntegerField(label='Wähle die maximale Anzahl der Fragen?', widget=forms.Select(choices=COUNT_CHOICE))
	
class ParaTestForm(forms.Form):
    arg1 = forms.CharField(max_length=50)
    #arg2 = forms.CharField(max_length=50)