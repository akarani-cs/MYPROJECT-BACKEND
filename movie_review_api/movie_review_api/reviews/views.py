from rest_framework import viewsets, permissions, decorators, response
from django.db.models import Q
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    filterset_fields = ['rating']
    search_fields = ['movie_title', 'content']
    ordering_fields = ['rating', 'created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @decorators.action(detail=False, methods=['get'], url_path='by-movie')
    def by_movie(self, request):
        title = request.query_params.get('title')
        qs = self.get_queryset()
        if title:
            qs = qs.filter(movie_title__icontains=title)
        page = self.paginate_queryset(qs)
        if page is not None:
            ser = self.get_serializer(page, many=True)
            return self.get_paginated_response(ser.data)
        ser = self.get_serializer(qs, many=True)
        return response.Response(ser.data)
