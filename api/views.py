# api/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import Book, Review
from .permissions import IsReviewOwner

from .serializers import (
    RegisterSerializer, BookSerializer,
    ReviewSerializer, ChangePasswordSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Change Password View
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'error': 'Wrong old password'}, status=400)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': 'Password changed successfully'})
        return Response(serializer.errors, status=400)

# Book Views
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [permissions.AllowAny()]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return [permissions.AllowAny()]

# Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, book_id=self.kwargs['book_id'])

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticated(), IsReviewOwner()]
        return [permissions.AllowAny()]

