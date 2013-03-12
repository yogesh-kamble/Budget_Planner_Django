from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Budget_Monitor.views.home', name='home'),
    # url(r'^Budget_Monitor/', include('Budget_Monitor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^transaction/', include("Transaction.urls")),
    url(r'^budget/', include("budget_manager.urls")),
    #url(r'people/$','Transaction.views.people'),
    url(r'home/$','home.views.home_page'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
