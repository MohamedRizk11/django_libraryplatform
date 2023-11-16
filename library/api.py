from  rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics,filters
from .serializers import autherserializer,bookserializer
from .models import Author , Book

@api_view(['GET'])
def author_list_api(request):
    authors=Author.objects.all()
    data = autherserializer(authors,many=True).data
    return Response({'Authors':data})

@api_view(['GET'])
def book_list_api(request):
    books=Book.objects.all()
    data = bookserializer(books,many=True).data
    return Response({'Books':data})

@api_view(['GET'])
def author_detail_api(request,id):
    authors=Author.objects.get(id=id)
    data = autherserializer(authors).data
    return Response({'Author':data})

class Booklistapi(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=bookserializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'price']
    search_fields = ['title', 'price', 'review']
    ordering_fields = ['review', 'publication_date']

class Bookdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=bookserializer
class Authorlistapi(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=autherserializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name', 'books']
    search_fields = ['name', 'biography', 'birth_date']
    ordering_fields = ['birth_date', 'books']
class Authordetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=autherserializer
    
