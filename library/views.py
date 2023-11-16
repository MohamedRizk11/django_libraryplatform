from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book ,Author

# Create your views here.
def mydebug(request):
    data=Book.objects.select_related('author').all()
    return render(request,'library/mydebug.html',{'data':data})





def book_list(request):
    all_books=Book.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_books, 40)
    try:
        all_books = paginator.page(page)
    except PageNotAnInteger:
        all_books = paginator.page(1)
    except EmptyPage:
        all_books = paginator.page(paginator.num_pages)
    return render(request,'library/book_list.html',{'books':all_books})


def book_detail(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,'library/book_detail.html',{'book':book})


def author_list(request):
    all_author=Author.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_author, 40)
    try:
        all_author = paginator.page(page)
    except PageNotAnInteger:
        all_author = paginator.page(1)
    except EmptyPage:
        all_author = paginator.page(paginator.num_pages)
    return render(request,'library/author_list.html',{'authors':all_author})


def author_detail(request,slug):
    author=Author.objects.get(slug=slug)
    return render(request,'library/author_detail.html',{'author':author})