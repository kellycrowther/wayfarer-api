from rest_framework import generics
from guest_books.models import GuestBook 
from guest_books.serializers import GuestBookSerializer
from rest_framework.permissions import IsAuthenticated

class GuestBookList(generics.ListCreateAPIView):
  queryset = GuestBook.objects.all()
  serializer_class = GuestBookSerializer

class GuestBookDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = GuestBook.objects.all()
  serializer_class = GuestBookSerializer
