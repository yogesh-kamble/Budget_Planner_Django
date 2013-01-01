# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from budget_manager.models import source,income
from budget_manager.income_form import Incomeform
from django.db.models import Sum


def process_income(request):
    '''
    '''
    income_status = False
    if request.method == "POST":
        form = Incomeform(request.POST)
        if form.is_valid():
            '''
            Store Income into database
            '''
            month = form.cleaned_data['month']
            income_source = form.cleaned_data['source_name']
            income_val = form.cleaned_data['income']
            income_source = dict(form.INCOME_SOURCE_CHOICES)[int(income_source)]
            source_obj = source.objects.filter(name=income_source)
            income_obj = income(source_id=source_obj[0].id, amount=income_val, income_month=month)
            income_obj.save()
            income_status = True
            
            
    else:
        form = Incomeform()
        return render_to_response ("add_income.html",{"form":form}, context_instance=RequestContext(request))
    del form
    return render_to_response("add_income.html",{"form":Incomeform(),"income_status":income_status},context_instance=RequestContext(request))


def display_income(request):
    '''
    Used For Displaying Income
    '''
    income_record_list=[]
    income_record_obj_list = income.objects.all()
    total_income=income_record_obj_list.aggregate(total_income=Sum('amount'))['total_income']
    for income_record in income_record_obj_list:
        source_name = source.objects.filter(id=income_record.source_id)[0].name
        income_record_list.append([income_record,source_name])
        
    return render_to_response('income_display.html',{"record_list":income_record_list,'total_income':total_income})
    
    
