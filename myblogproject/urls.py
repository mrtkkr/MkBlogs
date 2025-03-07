"""
URL configuration for myblogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('index/ornekMakale',views.ornekMakale,name="ornekMakale"),
    path('index/ornekMakale2',views.ornekMakale2,name="ornekMakale2"),
    path('index/ornekMakale3',views.ornekMakale3,name="ornekMakale3"),
    path('footer/contact',views.contact,name="contact"),
    path('footer/gizlilik',views.gizlilik,name="gizlilik"),
    path('footer/sartlar',views.sartlar,name="sartlar"),
    path('about/',views.about,name="about"),
    path('blogs/',include("blog.urls")),
    path('user/',include("user.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)