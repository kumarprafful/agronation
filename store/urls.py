from django.conf.urls import url
from .views import ItemListView, ItemDetailView, product_detail

app_name = 'store'

urlpatterns = [
	url(r'^$', ItemListView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', ItemDetailView.as_view(), name='item'),
	# url(r'^prodetail/(?P<id>[0-9]+)/$', product_detail, name='product_detail')
]