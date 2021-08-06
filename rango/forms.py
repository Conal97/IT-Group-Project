from django import forms
from django.forms import ModelForm, Textarea
from django.forms.fields import CharField
from rango.models import BaggedMunros, Hiker, Report
from django.contrib.auth.models import User
from rango.choices import *

# Form for profile picture change
class HikerProfileForm(forms.ModelForm):
    class Meta:
        model = Hiker
        fields = ('picture',)

# Form for hiker bagged munro change  
class HikerBaggedMunrosForm(forms.ModelForm):
    class Meta:
        model = Hiker
        fields = ('bagged',)

class HikeReportForm(forms.ModelForm):
    report_text = forms.CharField(max_length=3000, help_text='Enter your report here.')
    difficulty = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 

    class Meta:
        model = Report
        fields = ('difficulty', 'report_text')


class HikeReportForm(forms.ModelForm):
    report_text = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={"rows":8, "cols":85}))
    difficulty = forms.ChoiceField(label='Your challenge rating out of 5 ', widget=forms.Select, choices=CHOICES)

    class Meta:
        model = Report
        fields = ('difficulty', 'report_text')
        widgets = {
            'summary': Textarea(attrs={'rows':80, 'cols':20}),
        }
