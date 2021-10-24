# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Article
from .serializers import ArticleSerializer


from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from django_filters import rest_framework
from .permissions import IsOwnerOrReadOnly



'''
Because we're using viewsets instead of views, we can automatically generate the URL conf for our API, 
by simply registering the viewsets with a router class.
'''
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)



''' 
the one method 
'''
# class ArticleList(APIView):
#     # 先认证后分配权限
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ArticleDetail(APIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(instance=article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

'''
the other method
'''
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # pagination_class = MyPageNumberPagination  # 可在setting配置全局分页器

    # 根据关键字筛选 + 排序
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('title',)
    ordering_fields = ('create_date',)

    # 因为author是只读字段，所以这里在写入数据库的时候要手动绑定
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

