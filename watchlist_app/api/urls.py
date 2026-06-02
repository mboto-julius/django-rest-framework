from django.urls import path
from watchlist_app.api.views import StreamPlatformDetail, StreamPlatformList, WatchDetail, WatchListView

urlpatterns = [
    path('list/', WatchListView.as_view(), name='watch-list'),
    path('list/<int:pk>', WatchDetail.as_view(), name='watch-detail'),
    path('streams/', StreamPlatformList.as_view(), name='stream-platform-list'),
    path('streams/<int:pk>', StreamPlatformDetail.as_view(), name='stream-platform-detail'),
]
