from django.db import models
from budget_manager.models import Account
# Create your models here.

class Category(models.Model):
	name = models.CharField('name', max_length=100)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table="category" #Override Default behaviour of django table name creation
	

class Expense(models.Model):
	name=models.CharField('name', max_length=100)
	category=models.ForeignKey(Category)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table="expense" #Override Default behaviour of django table name creation
	

class Daily_Transaction(models.Model):
	account = models.ForeignKey(Account)
	category = models.ForeignKey(Category)
	amount_value = models.IntegerField('amount', max_length=100)
	description = models.CharField(max_length=100)
	transaction_date = models.DateField('transaction_date')
	
	def __unicode__(self):
		return str(self.id)
	class Meta:
		db_table="daily_transaction" #Override Default behaviour of django table name creation
		

		

	

	
