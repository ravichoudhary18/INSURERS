from django.urls import path
from file.views import FileView, DownloadAPIView

urlpatterns = [
    path('file-upload/', FileView.as_view(), name='save_file'),
    path('file-download/<int:pk>/', DownloadAPIView.as_view(), name='save_download'),
]
