'''
Created on 14-Jan-2013

@author: yogesh
'''
import pdb
from django.db.models import Sum
from budget_manager.models import *

class Income_Base:
    
    def __init__(self):
        '''
        '''
    
    def add_income(self, form):
        '''
        @Args: form object
        
        This method will add supplied income to database. 
        '''
        source = form.cleaned_data['Source_name']
        account = form.cleaned_data['Accout_name']
        income_val = form.cleaned_data['Income']
        recurrence = form.cleaned_data['Recurrence']
        date = form.cleaned_data['Date']
        
        #Add account and source to Account_Source_Map
        try:
            #Account and Source are unique so if it present use existing object.
            account_source_map_obj = Account_Source_Map.objects.get(source=source, account=account)
        except Account_Source_Map.DoesNotExist:
            account_source_map_obj = Account_Source_Map()
            account_source_map_obj.account=account
            account_source_map_obj.source=source
            account_source_map_obj.save()
        
        #Add Income to database
        income_obj = Income(account_source_map = account_source_map_obj, amount=income_val, recurrence = recurrence, income_date = date)
        
        #Add income amount to account
        account.balance += income_obj.amount
        account.save()
        income_obj.save()
        
        return
        
    def get_income(self):
        '''
        '''
        income_record_list=[]
        income_record_obj_list = Income.objects.all()
        total_income=income_record_obj_list.aggregate(total_income=Sum('amount'))['total_income']
        for income_record in income_record_obj_list:
            #source_name = Source.objects.filter(id=income_record.source_id)[0].name
            income_record_list.append(income_record)
            
        return (income_record_list, total_income)
        
    def check_for_recurrence(self):
        '''
        '''
        

class Account_Base:
    
    def __init__(self):
        '''
        '''
    
    def add_account(self,form):
        '''
        '''
        name=form.cleaned_data['name']
        balance=form.cleaned_data['balance']
        
        Account.objects.create(name=name, balance=balance)
        #account_obj.save()
        
        return
        
    
    def get_account(self):
        '''
        '''
        account_list = Account.objects.all()


if __name__ == "__main__":
    
    obj=Income_Base()        
        
    