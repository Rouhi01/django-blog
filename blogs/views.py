from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from.models import Blog, Category

class PostsByCategoryView(View):
    template_name = 'blogs/posts_by_category.html'
    def get(self, request, category_id):
        posts = Blog.objects.filter(status='Published', category=category_id)
        # try:
        #     category = Category.objects.get(id=category_id)
        # except:
        #     return redirect('home')
        category = get_object_or_404(Category, id=category_id)
        context = {
            'posts':posts,
            'category':category,
        }
        return render(request, self.template_name, context)
