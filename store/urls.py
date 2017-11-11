from django.conf.urls import url
from .views import ItemListView, ItemDetailView

app_name = 'store'

urlpatterns = [
	url(r'^$', ItemListView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', ItemDetailView.as_view(), name='item'),
]