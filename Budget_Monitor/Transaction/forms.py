from django import forms
import datetime
class People(forms.Form):
    '''
    '''
    Name = forms.CharField(initial="Yogesh kamble")
    Phone = forms.DateField(initial=datetime.date.today)
    Address = forms.Textarea() 