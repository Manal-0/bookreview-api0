# api/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, ChangePasswordView,
    BookListView, BookDetailView,
    ReviewListCreateView, ReviewDetailView
)

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('books/<int:book_id>/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
