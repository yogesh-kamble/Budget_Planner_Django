# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from budget_manager.income_form import Incomeform, Accountform
from income_base import Income_Base,Account_Base
import pdb

INCOME_OBJ = Income_Base()
ACCOUNT_OBJ = Account_Base()
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
            INCOME_OBJ.add_income(form)
            income_status = True
            
            return HttpResponseRedirect(reverse("budget_manager.views.process_income"))
    
    return render_to_response("add_income.html",{"form":Incomeform(),"income_status":income_status},context_instance=RequestContext(request))


def display_income(request):
    '''
    Used For Displaying Income
    '''
    (income_record_list, total_income)=INCOME_OBJ.get_income()
        
    return render_to_response('income_display.html',{"record_list":income_record_list,'total_income':total_income})
    

def create_account(request):
    '''
    '''
    if request.method == "POST":
        form_obj = Accountform(request.POST)
        if form_obj.is_valid():
            ACCOUNT_OBJ.add_account(form_obj)
            return HttpResponseRedirect(reverse("budget_manager.views.create_account"))
    
    return render_to_response("add_account.html",{"form":Accountform()}, context_instance=RequestContext(request))