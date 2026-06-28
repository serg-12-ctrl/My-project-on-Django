from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # 1. Сначала обрабатываем редирект с корня сайта http://127.0.0.1:8000/ на /projects/
    path('', RedirectView.as_view(url='projects/', permanent=True)),

    # 2. Обрабатываем стандартные маршруты приложений
    path('admin/', admin.site.urls), 
    path('projects/', include('projects.urls')), 
]

# 3. Статику и медиа-файлы подключаем СТРОГО в самом конце и только при DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
