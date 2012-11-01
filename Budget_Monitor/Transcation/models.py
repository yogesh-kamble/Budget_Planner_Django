from django.db import models

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
	

class Amount(models.Model):
	amount_value = models.IntegerField('amount', max_length=100)
	transaction_date = models.DateField('transaction_date')
	description = models.CharField('description', max_length=200)
	expense = models.ForeignKey(Expense)
	
	class Meta:
		db_table="amount" #Override Default behaviour of django table name creation
	

	
