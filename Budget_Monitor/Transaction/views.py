from models import Daily_Transaction ,Expense, Category
from transaction_forms import Daily_Transaction_form
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.db.models import Sum
import datetime
import pdb
# Create your views here.
        
def add_transaction(form_obj):
    '''
    '''
    account_obj = form_obj.cleaned_data['account']
    category_obj = form_obj.cleaned_data['category']
    amount_value = form_obj.cleaned_data['amount_value']
    description = form_obj.cleaned_data['description']
    transaction_date = form_obj.cleaned_data['transaction_date']
    
    transaction_obj = Daily_Transaction(account=account_obj, category=category_obj, amount_value= amount_value, \
                                        description=description, transaction_date=transaction_date)
    
    if account_obj.balance < amount_value:
        print "Hey Wait I need to think on this"
        return False
    transaction_obj.save()
    account_obj.balance -= amount_value
    account_obj.save()
    return True
    
def get_expense_details():
	'''
	Just get expense details and return the list
	'''
	#pdb.set_trace()
	expense_list = Daily_Transaction.objects.all()
	total_expense=expense_list.aggregate(total_expense=Sum('amount_value'))['total_expense']
	return (expense_list, total_expense)

def process_transaction(request):
    '''
    Method which render to add_transcation.html page.
    '''
    
    if (request.method == "POST"):
        form = Daily_Transaction_form(request.POST)
        if (form.is_valid()):
            if add_transaction(form):
                return HttpResponseRedirect(reverse('Transaction.views.process_transaction'))
            
    return render_to_response('add_transcation.html',{"form":Daily_Transaction_form()}, context_instance=RequestContext(request))    


def display_Expenses(request):
    '''
    '''
     
    #amount_obj = Amount()
    expense_amount_list=[]
    #record_list=Daily_Transaction.objects.all()
    (expense_list, total_expense) = get_expense_details()
    
    return render_to_response('display.html',{"expense_list":expense_list,"total_expense":total_expense})

def save_transaction(request):
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
        
        expense_obj=Category.objects.filter(name=expense)
        expense_id=expense_obj[0].id
        
        amount_obj = Amount(amount_value=amount, transaction_date=date, description=description, category_id=expense_id)
        amount_obj.save()
        
        return render_to_response("add_transcation.html", {"transaction_save_ack":"Saved your Transaction"},context_instance=RequestContext(request))
        
        
    
        
    
