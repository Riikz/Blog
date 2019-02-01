from django.urls import path
from . import views
from accounts import views as v

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.blog_create, name='create'),
    path('<int:pk>/', views.detail_view, name='detail'),
    path('detail/<int:pk>', views.DetailBlogView.as_view(), name='blog-detail'),
    path('detail/<int:blog_id>/comment', views.comment_create, name='comment'),
    path('detail/<int:pk>/edit', views.edit_blog, name='edit_blog'),
    path('detail/<int:pk>/delete', views.delete_blog, name='delete_blog'),
    path('<int:pk>/follow', v.follow_view, name='follow'),
    path('<int:pk>/unfollow', v.unfollow_view, name='unfollow'),
    path('<int:pk>/subscribe', v.subscribe_email, name='subscribe'),
    path('<int:pk>/unsubscribe', v.unsubscribe_email, name='unsubscribe'),
    path('generate', views.create_report, name='generate'),
    ]

