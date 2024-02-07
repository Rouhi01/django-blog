from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('<int:category_id>/', views.PostsByCategoryView.as_view(), name='posts_by_category'),
]