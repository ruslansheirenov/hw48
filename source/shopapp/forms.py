from django import forms
from django.forms import widgets


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100, required=True, label="Наименование")
    description = forms.CharField(max_length=2000, required=False, label="Описание", widget=widgets.Textarea(attrs={"rows": 5, "cols":50}))