from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Blog
class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())      
    class Meta:
        model = Blog
        fields = ("title","content","blog_image")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-lg", "style": "width: 100%;"}),
        }
    