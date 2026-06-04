from django.urls import include, path
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import StreamPlatformDetail, StreamPlatformList, StreamPlatformViewSet, WatchDetail, WatchListView, ReviewList, ReviewDetail, ReviewCreate

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListView.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetail.as_view(), name='watch-detail'),
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformList.as_view(), name='streamplatform-list'),
    # path('stream/<int:pk>', StreamPlatformDetail.as_view(), name='streamplatform-detail'),
    
    # path('reviews/', ReviewList.as_view(), name='review-list'),
    # path('reviews/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
