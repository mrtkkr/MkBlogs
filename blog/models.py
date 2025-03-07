from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Blog(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=70,verbose_name="başlık")
    content = CKEditor5Field("İçerik", config_name="default")  # CKEditor 5 kullanıldı
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    blog_image=models.FileField(blank=True,null=True,verbose_name="Bloğa Fotoğraf Ekleyin.")

    #admin panelinde blog_object1 diye yazmaz kullanıcının başlığı yazar.
    def __str__(self):
        return self.title
    class Meta:
        ordering= ['-created_date']
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length=300,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering= ['-comment_date']