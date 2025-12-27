from django.contrib import admin

from assignments.models import About
from .models import Category
from .models import Blog
from .models import Comment
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('title',)}
    list_display =('title','category','author','status','is_featured')
    search_fields =('id','title','category __category_name','status')


admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)

