from file_manager.services.file_signature_determinant import read_file
from test_site.celery import app

from file_manager.models import File


@app.task
def file_processing(file_pk):
    """
    функция асинхронной обработки файла
    :param file_pk: pk обрабаотываемого файла
    :return: None
    """
    file = File.objects.get(pk=file_pk)
    read_file(file.file)
    file.processed = True
    file.save()
