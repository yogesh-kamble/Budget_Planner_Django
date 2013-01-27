'''
Created on 09-Dec-2012

@author: yogesh
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('budget_manager.views',
              #This pattern contain all urls for budget app. 
            
              url(r'income/$', 'process_income'),
              url(r'view/$','display_income'),
              url(r'create_account/$','create_account')
)
