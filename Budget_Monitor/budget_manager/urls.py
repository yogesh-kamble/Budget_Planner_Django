'''
Created on 09-Dec-2012

@author: yogesh
'''
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from models import Account
urlpatterns = patterns('budget_manager.views',
              #This pattern contain all urls for budget app. 
            
              url(r'^add_income/$', 'process_income'),
              url(r'^view_income/$','display_income'),
              url(r'^create_account/$','create_account'),
              url(r'^view_account/$', ListView.as_view(queryset=Account.objects.all(),
                                               context_object_name="account_list",
                                               template_name="budget_manager/view_account.html")),
)
