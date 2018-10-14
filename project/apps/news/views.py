from .models import *
from .serializers import *
from rest_framework import generics


class NewsListCreate(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
