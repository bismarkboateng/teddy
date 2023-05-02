from django import forms 
from .models import Product 

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("created_by", )

        widgets={
            "category": forms.Select(attrs={
                "class": INPUT_CLASSES
            }),

            "price": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),

            "name": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),

            "description": forms.Textarea(attrs={
                "class": INPUT_CLASSES
            }),

            "image": forms.FileInput(attrs={
                "class": INPUT_CLASSES
            }),

        }




class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "description", "image", )

        widgets={

            "price": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),

            "name": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),

            "description": forms.Textarea(attrs={
                "class": INPUT_CLASSES
            }),

            "image": forms.FileInput(attrs={
                "class": INPUT_CLASSES
            }),

        }