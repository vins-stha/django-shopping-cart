# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 100, db_index = True)
	slug = models.SlugField(max_length =100, db_index = True, unique = True)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
		
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('product_list_by_category', args=[self.slug])
	
		
		
class Product(models.Model):
	category = models.ForeignKey(Category,related_name ='products', on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, db_index = True)
	slug = models.SlugField(max_length = 100, db_index = True)
	description = models.TextField(blank = True)
	price = models.DecimalField(max_digits = 100, decimal_places = 2)
	available = models.BooleanField(default = True)
	stock = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	#image = models.ImageField(blank = True)
	image = models.ImageField(blank = True, upload_to = 'products/%d/%m/%Y')
	
	class Meta:
		ordering = ('name',)
		index_together =(('id','slug'),)
		
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('product_detail', args=[self.id,self.slug])