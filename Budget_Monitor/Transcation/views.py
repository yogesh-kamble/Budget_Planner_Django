from models import Amount,Expense,Category
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
# Create your views here.

def enter_transcation(request):
    '''
    Method which render to add_transcation.html page.
    '''
    expense_obj_list=Expense.objects.all()
    
    expense_name_list=[expense.name for expense in expense_obj_list]
    
    return render_to_response('add_transcation.html',{"expense_list":expense_name_list}, context_instance=RequestContext(request))    


def display_Transaction(request):
    '''
    '''
     
    #amount_obj = Amount()
    expense_amount_list=[]
    record_list=Amount.objects.all()
    for record in record_list:
        expense_obj_list = Expense.objects.filter(id=record.expense_id)
        expense_name = expense_obj_list[0].name
        expense_amount_list.append([record,expense_name])
    
    return render_to_response('display.html',{"record_list":expense_amount_list})

def save_transcation(request):
    '''
    Method for saving Transcation
    '''
    
    if request.method == "POST":
        
        amount=request.POST["amount"]
        date=request.POST["date_pick"]
        description=request.POST['desc']
        expense=request.POST['expense_value']
        
        #change date format from dd-mm-yyyy to yyyy-mm-dd
        datetime_obj=datetime.datetime.strptime(date, "%d-%m-%Y")
        date=datetime_obj.strftime("%Y-%m-%d")
        
        expense_obj=Expense.objects.filter(name=expense)
        expense_id=expense_obj[0].id
        
        amount_obj = Amount(amount_value=amount, transaction_date=date, description=description, expense_id=expense_id)
        amount_obj.save()
        
        return render_to_response("add_transcation.html", {"transcation_save_ack":"Saved your Transcation"},context_instance=RequestContext(request))
        
        
    
        
    
