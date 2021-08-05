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




'''class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                            help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0) #even tho these are 
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0) #hidden still need to declare
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category #associate form and model
        fields = ('name',)

class PageForm(forms.ModelForm):

        title = forms.CharField(max_length = 128, help_text="Please enter the title of the page.")
        url = forms.URLField(max_length =200, help_text='Please enter the URL of the page.')
        views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        
        class Meta:
            model = Page
            exclude = ('category',)

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
