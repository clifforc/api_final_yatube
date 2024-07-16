from django.urls import path, include
from rest_framework_extensions.routers import ExtendedSimpleRouter

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router_v1 = ExtendedSimpleRouter()
(
    router_v1.register(r"posts", PostViewSet, basename="post").register(
        r"comments",
        CommentViewSet,
        basename="post-comments",
        parents_query_lookups=["post"],
    )
)
router_v1.register(r"groups", GroupViewSet, basename="group")
router_v1.register(r"follow", FollowViewSet, basename="folower")

urlpatterns = [
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router_v1.urls)),
]
