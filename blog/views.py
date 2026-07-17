from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blogs= Blog.objects.all()
    return render(request, 'extending/blogs.html',{'blogs': blogs})

def blog_detail(request, id):
    blog= get_object_or_404(Blog, id=id)
    return render(request, 'extending/blog_details.html',{'blog': blog})
