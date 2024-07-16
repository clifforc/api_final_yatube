from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, mixins

from posts.models import Group, Post, Comment, Follow
from api.serializers import (
    GroupSerializer,
    PostSerializer,
    CommentSerializer,
    FollowSerializer,
)
from api.permissions import AuthorAccessPermission


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorAccessPermission]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorAccessPermission]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs["parent_lookup_post"])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        parent_lookup_post = self.kwargs.get("parent_lookup_post")
        return (
            Comment.objects.filter(post_id=parent_lookup_post)
            if self.kwargs.get("parent_lookup_post")
            else Comment.objects.all()
        )
