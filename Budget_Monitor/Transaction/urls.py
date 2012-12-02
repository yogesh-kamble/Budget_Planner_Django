'''
Created on 02-Dec-2012

@author: yogesh
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Budget_Monitor.views.home', name='home'),
    # url(r'^Budget_Monitor/', include('Budget_Monitor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'view_transaction/', 'Transaction.views.display_Transaction'),
    url(r'enter_transaction/$','Transaction.views.enter_transaction'),
    url(r'enter_transaction/save_transaction','Transaction.views.save_transaction'),
)
