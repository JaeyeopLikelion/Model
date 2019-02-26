from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 데이터베이스에 저장
    return redirect('/blog/'+str(blog.id))

def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog_update.title = request.POST['title']
        blog_update.body = request.POST['body']
        blog_update.pub_date = timezone.datetime.now()
        blog_update.save()
        return redirect('detail', blog_id)
    else :
        return render(request, 'update.html', {'blog':blog_update})


def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')

    