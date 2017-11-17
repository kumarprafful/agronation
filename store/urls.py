from django.conf.urls import url
from .views import item_list, item_detail

app_name = 'store'

urlpatterns = [
 	url(r'^$', item_list, name='item_list'),
 	url(r'^(?P<category_slug>[-\w]+)/$', item_list, name='item_list_by_category'),
 	url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', item_detail, name='item_detail' ),
]




# 	url(r'^$', ItemListView.as_view(), name='index'),
# 	url(r'^(?P<pk>[0-9]+)/$', ItemDetailView.as_view(), name='item'),
	# url(r'^prodetail/(?P<id>[0-9]+)/$', product_detail, name='product_detail')
