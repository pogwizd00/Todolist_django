from django import forms
from django.forms import ModelForm
from .models import Todolist, Item, User


class ListForm(ModelForm):
    class Meta:
        model = Todolist
        fields = ('user','list_name','discription')
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'list_name': forms.TextInput(attrs={'class':'form-control'}),
            'discription': forms.TextInput(attrs={'class':'form-control'}),
        }

#diffrent forms for diffrent users 
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('item_name','item_date','todolist','desciption')
        widgets ={
            'item_name':forms.TextInput(attrs={'class':'form-control'}),
            'item_date':forms.DateTimeInput(attrs={'class':'form-control'}),
            'todolist':forms.Select(attrs={'class':'form-control'}),
            'desciption': forms.TextInput(attrs={'class':'form-control'}),
        }