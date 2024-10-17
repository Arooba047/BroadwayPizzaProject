from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['menu_name', 'menu_price', 'menu_image_url']

        widgets={
            'menu_name': forms.TextInput(attrs={'class':'form-control'}),
            'menu_price': forms.NumberInput(attrs={'class':'form-control', 'step': '0.01'}),
            'menu_image_url': forms.URLInput(attrs={'class':'form-control'})
        }

