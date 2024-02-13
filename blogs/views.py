from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from.models import Blog, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect

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

class BlogView(View):
    template_name = 'blogs/post_detail.html'
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Blog, slug=kwargs['slug'], status='Published')
        super().setup(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        post = self.post_instance
        comments = Comment.objects.filter(blog=post)
        comment_count = comments.count()

        context = {
            'comment_count':comment_count,
            'post':post,
            'comments':comments
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        post = self.post_instance
        comment = Comment()
        comment.user = request.user
        comment.blog = post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path)


class SearchView(View):
    template_name = 'blogs/search.html'
    def get(self, request):
        kw = request.GET.get('keyword')
        posts = Blog.objects.filter(Q(title__icontains=kw) | Q(short_description__icontains=kw) | Q(blog_body__icontains=kw), status='Published')
        context = {
            'posts':posts,
            'kw':kw
        }
        return render(request, self.template_name, context)