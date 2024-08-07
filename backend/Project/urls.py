from django.contrib import admin
from django.urls import path, include
from Project.views import ServerTest
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', ServerTest.as_view()),
    path('api/authentication/', include('authentication.urls'), name='authentication'),
    path('api/file/', include('file.urls'), name='file'),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)