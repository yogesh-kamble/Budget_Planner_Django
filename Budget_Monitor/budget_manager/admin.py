from budget_manager.models import *
from django.contrib import admin
#from Budget_Monitor.budget_manager.models import Account_Source_Map

class IncomeAdmin(admin.ModelAdmin):
    list_display = ("account_display", "source_display", "amount", "recurrence", "income_date")
    list_editable = ("income_date", "amount")
    list_filter = ("income_date",)
    date_hierarchy = "income_date"
    fieldsets = (
                  ('Account Source',{'fields':('account_source_map',)}),
                  ('Info',{'fields':('amount', 'recurrence', 'income_date')}),
                )
        
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "balance")
#admin.site.register(Budget_Type)
#admin.site.register(Budget)
#admin.site.register(Source)
admin.site.register(Income, IncomeAdmin)
#admin.site.register(Recurrence)
admin.site.register(Account, AccountAdmin)
admin.site.register(Account_Source_Map)
admin.site.register(Currency)