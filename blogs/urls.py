from .feeds import LatestPostFeed
from django.urls import path
from blogs import views

app_name = 'blogs'
urlpatterns = [
    path('', views.post_list, name='posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='detail'),
    path('<int:post_id>/share/', views.post_share, name='share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='posts_by_tag'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]