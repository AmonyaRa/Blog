from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.post.views import PostApiView, CommentApiView
from applications.post.views import CategoryApiView

router = DefaultRouter()
router.register('category', CategoryApiView)
router.register('comment', CommentApiView)
router.register('', PostApiView)


urlpatterns = [
    # path('', PostApiView.as_view({'get': 'list', 'post': 'create'})),
    # path('', include(router.urls))  # 2 метод написания router
]

urlpatterns += router.urls
