from django.conf.urls import include, url
from django.contrib import admin
from djangoapp.views import home,base, Property_entry,Property_list,sms
admin.site.site_header = 'Property Manager'
urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

url(r'^admin/', include(admin.site.urls)),
url(r'^$', 'djangoapp.views.home', name='home'),
url(r'^base/$', 'djangoapp.views.base',name='base'),
url(r'^Property_entry/$', 'djangoapp.views.Property_entry', name='Property_entry'),
url(r'^Property_list/$', 'djangoapp.views.Property_list', name='Property_list'),
url(r'^Property_list/Property_entry$', 'djangoapp.views.Property_entry', name='Property_entry'),
url(r'^Property_list/1(?P<id>\d+)/$', 'djangoapp.views.Property_edit', name='Property_edit'),
url(r'^accounts/', include('registration.backends.default.urls')),
url(r'^booking/', include('booking.urls')),
url(r'^sms/$', 'djangoapp.views.sms',name='sms'),
url(r'^say/$', 'django_twilio.views.say', {'text': 'hello, world!'}),
]
