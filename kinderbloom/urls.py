from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('class/', include('class.urls')),
    path('about/', include('about.urls')),
    path('team/', include('teacher.urls')),
    path('gallery/', include('gallery.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

