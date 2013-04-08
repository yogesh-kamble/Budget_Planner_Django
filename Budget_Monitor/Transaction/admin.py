from Transaction.models import Category, Expense, Daily_Transaction
from django.contrib import admin
from Transaction.transaction_forms import Daily_Transaction_form

class Expenses(admin.ModelAdmin):
    
    #form = Daily_Transaction_form
    list_display = ("account" ,"category", "description", "amount_value", "transaction_date")
    list_filter = ("category",)
    date_hierarchy = "transaction_date"
    fieldsets = (
                  ('Account Source',{'fields':('account',)}),
                  ('Info',{'fields':('category','description', 'amount_value', 'transaction_date')}),
                )

admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Daily_Transaction, Expenses)
