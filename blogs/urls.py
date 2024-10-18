from django.urls import path, include
from . import views

urlpatterns = [
    path('my-blogs/', views.myBlogs),
    path('blogs/<mySlug>', views.readBlog),
    path('my-blogs/write/', views.writeBlog),
    path('my-blogs/delete/<mySlug>', views.deleteBlog),
    path('my-blogs/update/<mySlug>', views.updateBlog),
    path('blogs/', views.allBlogs)
]