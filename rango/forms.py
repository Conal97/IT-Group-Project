from django import forms
from django.forms import fields
from django.forms.fields import CharField
from rango.models import BaggedMunros, Hiker, Report
from django.contrib.auth.models import User


class HikerProfileForm(forms.ModelForm):
    class Meta:
        model = Hiker
        fields = ('picture',)

    
class HikerBaggedMunrosForm(forms.ModelForm):
    class Meta:
        model = Hiker
        fields = ('bagged',)

    def clean(self):
        cleaned_data = self.cleaned_data
        bagged_string = cleaned_data.get('bagged')


class HikeReportForm(forms.ModelForm):
    report_text = forms.CharField(max_length=3000, help_text='Enter your report here.')
    difficulty = forms.IntegerField(widget=forms.HiddenInput(), initial=0) 

    class Meta:
        model = Report
        fields = ('difficulty', 'report_text')


'''
        def clean(self):
            cleaned_data = self.cleaned_data
            url = cleaned_data.get('url')


            if url and not url.startswith('http://'):
                url = f'http://{url}'
                cleaned_data['url']=url

            return cleaned_data'''



class HikeReportForm(forms.ModelForm):
    report_text = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={"rows":15, "cols":170}))
    # difficulty = forms.IntegerField(initial=1, help_text='Rate the challenge out on a scale of 1-10') 
    Options = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
     )
    select = forms.ChoiceField(label='Your challenge rating out of 5 ', widget=forms.Select, choices=Options)
    # author = Hiker.objects.get()
    class Meta:
        model = Report
        fields = ('select', 'report_text')
