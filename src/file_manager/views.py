from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from file_manager.models import File
from file_manager.serializers import FileSerializer
from file_manager.tasks import file_processing


class FileCreateView(CreateAPIView):
    """
    api view класс для загрузки и последующей обработки файли
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            file_processing.delay(file.pk)
            return Response(
                serializer.data,
                status=201
            )

        return Response(serializer.errors, status=400)


class FileListView(ListAPIView):
    """
    api view класс возвращающий все файлы и данные о них
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

