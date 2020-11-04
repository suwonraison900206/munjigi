from rest_framework import generics, status
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import ReviewSerializer, ReviewListSerializer
from .models import Review
from backend.pagination import CustomPagination
from django.db.models import Q

class ReviewListAPI(GenericAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = CustomPagination

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        
        if page is not None:
            serializer = ReviewListSerializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = ReviewListSerializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        

class ReviewListAPI2(GenericAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = CustomPagination
    def get(self, request):
        query = request.GET.get('query', '')
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(Q (title__icontains=query))
        page = self.paginate_queryset(queryset)
            
        if page is not None:
            serializer = ReviewListSerializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = ReviewListSerializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ReviewListAPI3(GenericAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = CustomPagination
    def get(self, request):
        query = request.GET.get('query', '')
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(Q (user=query))
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = ReviewListSerializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = ReviewListSerializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ReviewListAPI2(GenericAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = CustomPagination


    def get(self, request):
        query = request.GET.get('query', '')
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(title__icontains=query)
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = ReviewListSerializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = ReviewListSerializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ReviewDetailAPI(generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)
    

    def put(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    def delete(self, request, pk):
        queryset = get_object_or_404(Review, pk=pk)
        queryset.delete()
        return Response(True)
        