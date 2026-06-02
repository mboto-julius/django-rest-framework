from django.urls import path
from watchlist_app.api.views import ListMovies, MovieDetail
# from watchlist_app.api.views import movie_list, movie_detail 

urlpatterns = [
    path('list/', ListMovies.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie-detail'),
]
