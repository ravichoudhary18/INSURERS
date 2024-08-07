from django.urls import path
from file.views import FileView

urlpatterns = [
    path('file-upload/', FileView.as_view(), name='save_file'),
]
