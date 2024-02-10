from django.views import View
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from assignments.models import About
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
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

class RegisterView(View):
    template_name = 'register.html'
    form_clas = RegisterForm
    def get(self, request):
        form = RegisterForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            context = {
                'form':form
            }
            return render(request, self.template_name, context)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = authenticate(password=password, username=username)
            if user is not None:
                login(request, user)
            return redirect('home')
        else:
            context = {
                'form':form
            }
            return render(request, self.template_name, context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')