from django.http import HttpResponse,HttpResponseForbidden
from django.shortcuts import render
from blogs.models import Category,Blog
from django.shortcuts import get_object_or_404

def home(request):
    
    featured_posts =Blog.objects.filter(is_featured =True, status='Published').order_by('updated_at')
    posts =Blog.objects.filter(is_featured =False, status='Published')


    context ={
        'featured_posts':featured_posts,
        'posts':posts,
    }
    return render(request, 'home.html',context)
    return  render(request, 'home.html')







