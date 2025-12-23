

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('<int:category_id>/',views.post_by_category,name='post_by_category')
    
      
    # path('post/<int:post_id>/edit/',views.edit_post,name='edit_post'),

      
] +static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

