from django.contrib import admin
from django.urls import path

from blog import views

app_name="blog"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addblog/',views.addBlog,name="addblog"),
    path('update/<int:id>',views.updateBlog,name="update"),
    path('delete/<int:id>',views.deleteBlog,name="delete"),
    path('blog/<int:id>',views.detail,name="detail"),
    path('',views.blogs,name="blogs"),
    path('comment/<int:id>',views.addComment,name="comment"),
]