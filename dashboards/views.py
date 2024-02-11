from django.shortcuts import render, redirect
from django.views import View
from blogs.models import Blog, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddCategoryForm, EditCategoryForm


class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboards/dashboard.html'
    login_url = 'login'

    def get(self, request):
        category_count = Category.objects.all().count()
        blog_count = Blog.objects.all().count()

        context = {
            'category_count':category_count,
            'blog_count':blog_count
        }
        return render(request, self.template_name, context)


class CategoriesView(LoginRequiredMixin, View):
    template_name = 'dashboards/categories.html'
    def get(self, request):
        return render(request, self.template_name)


class AddCategoryView(LoginRequiredMixin, View):
    template_name = 'dashboards/add_category.html'
    form_class = AddCategoryForm

    def get(self, request):
        form = AddCategoryForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboards:categories')
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class EditCategoryView(LoginRequiredMixin, View):
    template_name = 'dashboards/edit_category.html'
    form_class = EditCategoryForm

    def setup(self, request, *args, **kwargs):
        self.category_instance = Category.objects.get(id=kwargs['category_id'])
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = EditCategoryForm(instance=self.category_instance)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = EditCategoryForm(request.POST, instance=self.category_instance)
        if form.is_valid():
            form.save()
            return redirect('dashboards:categories')
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class DeleteCategoryView(LoginRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        self.category_instance = Category.objects.get(id=kwargs['category_id'])
        super().setup(request, *args, **kwargs)
    def get(self, request, category_id):
        self.category_instance.delete()
        return redirect('dashboards:categories')
