from django.urls import path
from .views import ReviewListAPI, ReviewDetailAPI, ReviewListAPI2, ReviewListAPI3

urlpatterns = [
    path('', ReviewListAPI.as_view()),
    path('<int:pk>/', ReviewDetailAPI.as_view()),
    path('search/title/', ReviewListAPI2.as_view()),
    path('search/name/', ReviewListAPI3.as_view()),
]