from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import Blog
from .models import Category
from django.db.models import Q

def post_by_category(request, category_id):
    #fetch the posts that belogs to category with the id category_id
    posts =Blog.objects.filter(status='Published', category=category_id)
    #use try/except when we want to do some custom action if the category does not exisis
    try:
        category =Category.objects.get(pk=category_id)
    except:
        #redirect to the home page
        return redirect('home')
   # use get_objet_404 when you want to show 404 error page if the category does not exists.
    # category =get_object_or_404(Category,pk=category_id)


    context={
        'posts':posts,
        'category':category,
        
    }
    return render(request,'post_by_category.html',context)


def blogs(request,slug):
    single_blog =get_object_or_404(Blog,slug=slug, status='Published')
    context ={
        'single_blog':single_blog,
    }

    return render(request,'blogs.html',context)



def search(request):
    keyword =request.GET.get('keyword')
    blogs =Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) |Q(blog_body__icontains=keyword), status='Published')
    context ={
        'blogs':blogs,
        'keyword':keyword,

    }   
    return render(request, 'search.html',context)


