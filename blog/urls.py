from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # url(r'^/users/', generics.ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer),
    #     name='user-list'),
    path('users/', views.UserList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/', views.PostCreateList.as_view())
]
