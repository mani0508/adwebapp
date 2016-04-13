from django.conf.urls import include, url
from django.contrib import admin
# from codes.views import *
import codes.views
admin.site.site_header = 'ApexViz Administration'
urlpatterns = [
    # Examples:
    # url(r'^$', 'vishal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', codes.views.index),
    url(r'^login',codes.views.login),
    url(r'^logout',codes.views.logout),
    url(r'^register',codes.views.register),
    url(r'^upload',codes.views.upload_hoarding),
    url(r'^owner-hoarding-list',codes.views.owner_hoarding_list),
    url(r'^owner-transaction-history',codes.views.owner_transaction),
]
