from django.shortcuts import render
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from applications.post.models import Post, Category
from applications.post.permissions import IsOwner
from applications.post.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.

# class PostApiView(ViewSet):
#     def list(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10


class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'owner']
    search_fields = ['title', 'description']
    ordering_fields = ['id']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # с токена берет owner -> serializers

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     filter_ = self.request.query_params.get('category')
    #
    #     if filter_:
    #         queryset = queryset.filter(category=filter_)
    #     return queryset
