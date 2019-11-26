from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.CommentDetail.as_view(), name='thread'),
    path('', views.CommentList.as_view(), name='comment-list')
]
