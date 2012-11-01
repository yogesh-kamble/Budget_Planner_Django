from models import Amount,Expense,Category
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.

def enter_transcation(request):
    '''
    Method which render to add_transcation.html page.
    '''
    expense_obj_list=Expense.objects.all()
    
    expense_name_list=[expense.name for expense in expense_obj_list]
    
    return render_to_response('add_transcation.html',{"expense_list":expense_name_list})    


def display_Transaction(request):
    '''
    '''
    response=HttpResponse()
    response.write("<html>")
    response.write("<H1>Transcation Details</H1>")
    response.write("<body>")
    #amount_obj = Amount()
    record_list=Amount.objects.all()
    
    for record in record_list:
        response.write("<p> Your Amount is %d </p>"%record.amount_value)
        response.write("<p> Date of your Transcation %s </p>"%record.transaction_date)
        expense_obj_list = Expense.objects.filter(id=record.expense_id)
        expense_name = expense_obj_list[0].name
        response.write("<p> Expense Name : %s"%expense_name)
    response.write("</body></html>")
    
    return response

def save_transcation(request):
    '''
    Method for saving Transcation
    '''
    
        
    
