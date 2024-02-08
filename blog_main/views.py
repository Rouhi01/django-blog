from django.views import View
from django.shortcuts import render
from blogs.models import Category, Blog
from assignments.models import About
class HomeView(View):
    template_name = 'home.html'
    def get(self, request):
        categories = Category.objects.all()
        try:
            about = About.objects.get()
        except:
            about = False
        featured_posts = Blog.objects.filter(is_featured=True).order_by('updated_at')
        normal_posts = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
        context = {
            'about':about,
            'featured_posts': featured_posts,
            'normal_posts': normal_posts
        }
        return render(request, self.template_name, context)