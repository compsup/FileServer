from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('files/', views.files, name='files'),
    path('user/<str:user_name>/', views.user_profile, name='user_profile'),
    path('docs/', views.docs, name='docs'),
    path('files/upload/', views.files_upload, name='files_upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
