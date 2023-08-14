from django.urls import path
from .views import create_post,view_posts,DeletePost

urlspatterns= [
    path('create/',create_post,name='create-post'),
    path('view/',view_posts,name='view-posts'),
    path('delete/<int:post_id>/',DeletePost,name='delete-post'),
]