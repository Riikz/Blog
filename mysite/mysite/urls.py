from django.contrib import admin
from django.urls import include, path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.url')),
    path('accounts/', include('accounts.url')),
    path('', views.index, name="home"),
    path('auth/', include('social_django.urls', namespace="social")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'home'
