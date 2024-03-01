import time

from file_manager.services.file_signature_determinant import read_file
from test_site.celery import app

from file_manager.models import File


@app.task
def file_processing(file_pk):
    print(file_pk)
    file = File.objects.last()
    print(file)
    print(file.pk)
    print(file.processed)
    # file = File.objects.get(pk=file_pk)
    # read_file(file.file)
    file.processed = True
    print(file.processed)
    file.save()
    print(file.processed)
    file = File.objects.last()
    print(file)
    print(file.pk)
    print(file.processed)
    return True
