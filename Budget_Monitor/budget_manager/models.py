from django.db import models

# Create your models here.

class Budget_Type(models.Model):
    '''
    '''
    set_budget = models.CharField('budget_type', max_length = 100)
    
    class Meta:
        db_table = "budget_type"


class Budget(models.Model):
    '''
    '''
    budget_value = models.IntegerField('budget_value', max_length=100)
    budget_type_id = models.ForeignKey(Budget_Type)
    
    class Meta:
        db_table = "budget"
        


class Source(models.Model):
    '''
    '''
    name = models.CharField('name', max_length =100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = "source"


class Recurrence(models.Model):
    '''
    '''
    recurrence_type=models.CharField('recurrence_type', max_length=100)
    
    def __unicode__(self):
        return self.recurrence_type
    
    class Meta:
        db_table="recurrence"

class Account(models.Model):
    '''
    '''
    name=models.CharField(max_length=100)
    balance=models.IntegerField('balance', max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table="account"

class Account_Source_Map(models.Model):
    '''
    '''
    source = models.ForeignKey(Source)
    account = models.ForeignKey(Account)
    
    class Meta:
        db_table="account_source_map"

class Income(models.Model):
    '''
    '''
    account_source_map = models.ForeignKey(Account_Source_Map)
    amount = models.IntegerField('amount', max_length=100)
    recurrence=models.ForeignKey(Recurrence)
    income_date = models.DateField('income_month')
    
    def source_display(self):
        return ("%s"%self.account_source_map.source)
    def account_display(self):
        return ("%s"%self.account_source_map.account)
    
    source_display.short_description = "Income Source"
    account_display.short_description = "Account"
    
    class Meta:
        db_table = "income"
        
class Currency(models.Model):
    '''
    '''
    currency_type=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.currency_type
    
    class Meta:
        db_table="currency"

class Networth(models.Model):
    '''
    '''
    networth_value = models.IntegerField('networth_value', max_length=100)
    
    class Meta:
        db_table = "networth"