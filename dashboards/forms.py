from django import forms
from blogs.models import Category

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

