
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'demoapp.views.html_login', name='default page'),
    url(r'^login', 'demoapp.views.html_login', name='login page'),
    url(r'^logout', 'demoapp.views.html_logout', name='logout'),
    url(r'^register', 'demoapp.views.register', name='register page'),
    url(r'^index', 'demoapp.views.index', name='register page'),
    url(r'^config', 'demoapp.views.configureuser', name='configureuser page'),
    url(r'^active', 'demoapp.views.html_active', name='active'),
    url(r'^deactive', 'demoapp.views.deactive', name='deactive'),
    url(r'^launchinstance', 'demoapp.views.launchinstance', name='launchinstance'),


]
