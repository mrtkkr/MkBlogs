from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,reverse

from blog.models import Blog,Comment
from .forms import BlogForm
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def blogs(request):

    keyword=request.GET.get("keyword")
    if keyword:
        blogs=Blog.objects.filter(title__contains=keyword)
        return render(request,"blogs.html",{"blogs":blogs})
    
    blogs =Blog.objects.all()

    return render(request,"blogs.html",{"blogs":blogs})

def index(request):
    return render(request,"index.html")

def ornekMakale(request):
    return render(request,"ornekMakale.html")

def ornekMakale2(request):
    return render(request,"ornekMakale2.html")

def ornekMakale3(request):
    return render(request,"ornekMakale3.html")

def contact(request):
    storage = get_messages(request)  # Önceki mesajları temizle
    for _ in storage:
        pass  # Mesajları tüket
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        try:
            send_mail(
                subject=f"Yeni Mesaj: {name}",  # Konu başlığı
                message=f"Ad: {name}\nE-posta: {email}\n\nMesaj:\n{message}",
                from_email=settings.EMAIL_HOST_USER,  # Gönderici sen oluyorsun
                recipient_list=[settings.EMAIL_HOST_USER],  # Mesaj sana geliyor
                fail_silently=False,
            )
            messages.success(request, "Mesajınız başarıyla gönderildi!")
        except Exception as e:
            messages.error(request, f"Bir hata oluştu: {e}")
        return redirect('contact')  # Sayfayı yönlendirerek mesajı temizle



    return render(request,"contact.html")

def gizlilik(request):
    return render(request,"gizlilik_politikasi.html")
def sartlar(request):
    return render(request,"sartlar_ve_kosullar.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    blogs = Blog.objects.filter(author=request.user)
    context= {
        "blogs":blogs
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addBlog(request):
    form =BlogForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        blog= form.save(commit=False)
        blog.author=request.user
        blog.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu.")
        return redirect("blog:dashboard")
    return render(request,"addblog.html",{"form":form})
@login_required(login_url="user:login")
def deleteBlog(request,id):
    blog=get_object_or_404(Blog,id=id)
    blog.delete()
    messages.success(request,"Makale Başarıyla Silindi.")
    return redirect("blog:dashboard")

@login_required(login_url="user:login")
def updateBlog(request,id):
    blog=get_object_or_404(Blog,id=id)
    form =BlogForm(request.POST or None,request.FILES or None,instance=blog)
    if form.is_valid():
        blog= form.save(commit=False)
        blog.author=request.user
        blog.save()
        messages.success(request,"Makale Başarıyla Güncellendi.")
        return redirect("blog:dashboard")
    return render(request,"update.html",{"form":form})

def detail(request,id):
    #blog = Blog.objects.filter(id=id).first()
    blog=get_object_or_404(Blog,id=id)
    #models de releated_name değerini comments verdiğim için burda kullanabilirim.
    comments= blog.comments.all()
    return render(request,"detail.html",{"blog":blog,"comments":comments})

def addComment(request,id):
    blog=get_object_or_404(Blog,id=id)
    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        parent_id = request.POST.get("parent_id")

        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.blog=blog
        if parent_id:  # Eğer parent_id varsa, bu bir alt yorumdur.
            parent_comment = Comment.objects.get(id=parent_id)
            newComment.parent = parent_comment
        newComment.save()
    return redirect(reverse("blog:detail",kwargs={"id":id}))