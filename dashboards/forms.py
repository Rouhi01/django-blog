from django import forms
from blogs.models import Category, Blog


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured']


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured']
