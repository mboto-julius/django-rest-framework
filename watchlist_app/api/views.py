from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  
    
class StreamPlatformViewSet(viewsets.ViewSet):
    
    def list(self, request): 
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

class StreamPlatformList(APIView):
    
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetail(APIView):
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {'error': 'Stream platform not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {'error': 'Stream platform not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, pk): 
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {'error': 'Stream platform not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListView(APIView):
    
    def get(self, request):
        watchlists = WatchList.objects.all()
        serializer = WatchListSerializer(watchlists, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
           
class WatchDetail(APIView):
    
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {'error': 'Watchlist not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {'error': 'Watchlist not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, pk): 
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {'error': 'Watchlist not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
