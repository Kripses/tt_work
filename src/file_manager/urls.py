from django.urls import path

from file_manager.views import FileCreateView, FileListView

app_name = 'file_manager'

urlpatterns = [
    path('upload/', FileCreateView.as_view(), name='file_upload'),
    path('files/', FileListView.as_view(), name='file_list'),
]
