from django.db import models

# Create your models here.

class budget_type(models.Model):
    '''
    '''
    set_budget = models.CharField('budget_type', max_length = 100)
    
    class Meta:
        db_table = "budget_type"


class budget(models.Model):
    '''
    '''
    budget_value = models.IntegerField('budget_value', max_length=100)
    budget_type_id = models.ForeignKey(budget_type)
    
    class Meta:
        db_table = "budget"
        


class source(models.Model):
    '''
    '''
    name = models.CharField('name', max_length =100)
    
    class Meta:
        db_table = "source"


class income(models.Model):
    '''
    '''
    source = models.ForeignKey(source)
    amount = models.IntegerField('amount', max_length=100)
    month = models.DateField('month')
    
    class Meta:
        db_table = "income"
        


class networth(models.Model):
    '''
    '''
    networth_value = models.IntegerField('networth_value', max_length=100)
    
    class Meta:
        db_table = "networth"