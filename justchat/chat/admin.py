from django.contrib import admin
from .models import Post
# Register your models here.
#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
#    list_display=['id','title','auth','created-date']
     list_display=['id','title','created_date'] 
     list_display_links=['title'] 
     # list_editable=['is_public']
