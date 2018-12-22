from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,10)]

class CartAddProduct(forms.Form):
	quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES, coerce = int)
	update = forms.BooleanField(required = Flase, initial = False, widget = forms.HiddenInput)