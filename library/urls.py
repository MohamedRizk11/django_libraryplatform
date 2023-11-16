from django.urls import path
from .views import book_list,book_detail,author_list,author_detail,mydebug
from .api import author_list_api,book_list_api,author_detail_api,Booklistapi,Bookdetailapi,Authorlistapi,Authordetailapi

urlpatterns = [
    path('', author_list),
    path('books/', book_list),
    path('mydebug/', mydebug),
    path('<slug:slug>', author_detail),
    path('books/<slug:slug>', book_detail), 
    path('api/list',Authorlistapi.as_view()),
    path('books/api/list',Booklistapi.as_view()),
    path('api/list/<int:pk>',Authordetailapi.as_view()),
    path('books/api/list/<int:pk>',Bookdetailapi.as_view()),



]
