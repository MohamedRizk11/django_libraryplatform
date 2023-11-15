from django.contrib import admin
from .models import Book,Author,Review

# Register your models here.



class bookadmin(admin.ModelAdmin):
    list_display=['title','author','publication_date','price']
    search_fields=['title','author','price']
    list_filter=['price','publication_date']




admin.site.register(Book,bookadmin)
admin.site.register(Author)
admin.site.register(Review)
