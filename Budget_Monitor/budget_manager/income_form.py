'''
Created on 09-Dec-2012

@author: yogesh
'''
from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from budget_manager.models import source
from datetime import date

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

def get_source_list():
    '''
    return income source_list
    '''
    source_list=[]
    source_obj = source.objects.all()
    
    #source_name_list = [src.name for src in source_obj]
    for src in source_obj:
        source_list.append((src.id, src.name))
    return source_list




class Incomeform(forms.Form):
    '''
    This is form for entering income detail
    '''
    INCOME_SOURCE_CHOICES = tuple(get_source_list())
    source_name = forms.ChoiceField(choices = INCOME_SOURCE_CHOICES)
    income = forms.IntegerField(help_text="Enter your monthly Income")
    month = forms.DateField(widget = SelectDateWidget, required=False)
    
    