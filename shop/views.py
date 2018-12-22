# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import Category, Product

# Create your views here.
def product_list(request,category_slug = None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available = True)
	num_visits = request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits + 1

	if category_slug:
		category = get_object_or_404(Category, slug = category_slug)
		products = Product.objects.filter(category = category)
	context = {
			'category' : category,
			'categories':categories,
			'products':products,
			'num_visits':num_visits
		}
	return render(request,'shop/product/list.html',context)

		
def product_detail(request,id,slug):	
	product = get_object_or_404(Product,id = id, slug = slug, available = True)
	context = {
		'product':product
	}
	return render(request,'shop/product/detail.html',context)

def addToCart(request,id):
	text = None
	
	if request.method == "POST":
		text = 'hello world'
		context = {
			'id' :id,
			'text':text
			}
	return render(request, 'shop/product/success.html', context)
			