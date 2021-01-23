# -*- coding: utf-8 -*-
from django import forms
from .models import Products  #importing our model class from models.py

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields=['Item', 'Description', 'Price']  # class attributes of models.py
        
        

