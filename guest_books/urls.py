from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from guest_books import views

urlpatterns = [
  path('guest-books/', views.GuestBookList.as_view()),
  path('guest-books/<int:pk>/', views.GuestBookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
