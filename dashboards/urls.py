from django.urls import path
from . import views

app_name = 'dashboards'
urlpatterns = [
    #Dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),

    #Category
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('categories/add/', views.AddCategoryView.as_view(), name='add_category'),
    path('categories/edit/<int:category_id>/', views.EditCategoryView.as_view(), name='edit_category'),
    path('categories/delete/<int:category_id>/', views.DeleteCategoryView.as_view(), name='delete_category'),

    #Blog
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('posts/add/', views.AddPostView.as_view(), name='add_post'),
    path('posts/edit/<int:post_id>/', views.EditPostView.as_view(), name='edit_post'),
    path('posts/delete/<int:post_id>/', views.DeletePostView.as_view(), name='delete_post'),

]