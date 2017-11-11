from django.conf.urls import url

from django.contrib.auth.views import login, logout

from .views import register

app_name = 'accounts'

urlpatterns = [
	url(r'^register/$', register, name='register'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),

]