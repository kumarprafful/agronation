from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.

class ItemListView(ListView):
	model = Item
	template_name = 'index.html'
	context_object_name = 'items'

class ItemDetailView(DetailView):
	model = Item
	template_name = 'item_detail.html'
	context_object_name = 'item_detail'



