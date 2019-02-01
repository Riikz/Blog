from django.urls import path
from . import views
from blog.views import detail_view

app_name = 'accounts'

urlpatterns=[
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit', views.edit_view, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
]