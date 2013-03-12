'''
Created on 09-Dec-2012

@author: yogesh
'''
from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from budget_manager.models import Source,Recurrence,Account
from datetime import date
import pdb

class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        days = ((1,"Sunday"),(2,"Monday"))
        months = ((1,"Jan"),(2,"feb"))
        
        years = [(year, year) for year in (2011, 2012, 2013)]
        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(day=int(datelist[0]), month=int(datelist[1]),
                    year=int(datelist[2]))
        except ValueError:
            return ''
        else:
            return str(D)

# Subclass ModelChoiceField to return name of source for representing it on html.
class SourceChoiceField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        '''
        '''
        return obj.name

class AccountChoiceField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        return obj.name


class RecurrenceChoiceField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        return obj.recurrence_type



class Incomeform(forms.Form):
    '''
    This is form for entering income detail
    '''
    Source_name = SourceChoiceField(queryset = Source.objects.all(),  empty_label=None)
    Accout_name = AccountChoiceField(queryset = Account.objects.all(), empty_label = None)
    Recurrence = RecurrenceChoiceField(queryset = Recurrence.objects.all(), empty_label=None)
    Income = forms.IntegerField(help_text="Enter your monthly Income")
    Date = forms.DateField(widget = SelectDateWidget, required=False)
    
class Accountform(forms.Form):
    '''
    This is form for enetering your budget.(Main Goal of Budget_Planner)
    '''
    name = forms.CharField(max_length=50)
    balance = forms.IntegerField()
    
    