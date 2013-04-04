'''
Created on 10-Feb-2013

@author: yogesh
'''
from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from budget_manager.models import Account
from Transaction.models import Category
from datetime import date


TEXT_AREA_ATTRS={'rows':'3', 'cols':'3'}
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
class AccountChoiceField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        return obj.name

class CategoryChoiceField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        return obj.name

class Daily_Transaction_form(forms.Form):
    '''
    '''
    account = AccountChoiceField(queryset = Account.objects.all(), empty_label = None)
    category = CategoryChoiceField(queryset=Category.objects.all(), empty_label = None)
    amount_value = forms.IntegerField(label='amount')
    description = forms.CharField(widget=forms.Textarea(TEXT_AREA_ATTRS))
    transaction_date = forms.DateField(widget = SelectDateWidget, required=False)
