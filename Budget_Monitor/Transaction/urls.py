'''
Created on 02-Dec-2012

@author: yogesh
'''
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from models import Daily_Transaction
urlpatterns = patterns('Transaction.views',
    # Examples:
    # url(r'^$', 'Budget_Monitor.views.home', name='home'),
    # url(r'^Budget_Monitor/', include('Budget_Monitor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^view/$', 
    #        ListView.as_view(queryset=Daily_Transaction.objects.all(), 
    #                           template_name="transaction/display.html")),
    url(r'^view/$', 'display_Expenses'),
    url(r'enter/$','process_transaction'),
    url(r'save/$','save_transaction'),
)
