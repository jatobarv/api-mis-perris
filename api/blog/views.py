from .models import Post
from rest_framework import viewsets
from blog.serializers import PostSerializer

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('name')
    serializer_class = PostSerializer
