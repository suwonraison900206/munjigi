from django.db import models
from django.conf import settings
from heritage.models import Heritage


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= "user_review")
    heritage = models.ForeignKey(Heritage, on_delete=models.CASCADE, related_name="heritage_reviews")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_recommend = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="recommend_reviews", blank=True)