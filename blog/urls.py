from django.urls import path
from .views import  ListPost , PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
urlpatterns  = [
    path('' ,ListPost.as_view(), name = 'blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-post'),
    path('post/new/', PostCreateView.as_view(), name = 'create-post'),
    path('about/', views.about, name = 'blog-about')
]