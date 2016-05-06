import logging
import os

from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from mysite import settings
from random import randint
from mydrive.forms import UploadFileForm
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from drive.models import File
from drive.models import Repository

logger = logging.getLogger(__name__)

# class FileUploadView(APIView):
# parser_classes = (FileUploadParser, )


def getNewFileName(full_name):

    td = datetime.now()
    file_name, file_extension = os.path.splitext(full_name)
    new_full_name = file_name + "_" + \
        td.strftime('%Y-%m-%d-%H%M%S') + "_" + \
        str(randint(1, 10000)) + file_extension

    return os.path.join(settings.MEDIA_ROOT, new_full_name)


def post(request):

    for key, value in request.POST.items():
        print(key)
    # print(request.FILES)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        response_data = {}
        if form.is_valid():
                # newdoc = Document(docfile = request.FILES['docfile'])
                # newdoc.save()
            up_file = request.FILES['file']
            new_file_name = getNewFileName(up_file.name)
            destination = open(new_file_name, 'wb+')
            for chunk in up_file.chunks():
                destination.write(chunk)

            destination.close()

            response_data['status'] = "ok"
            response_data['name'] = up_file.name
            response_data['new_file_name'] = new_file_name
            response_data['description'] = "Your file has been uploaded:"
            response_data['size'] = str(up_file.size)
            response_data['content_type'] = up_file.content_type

            print(request.POST['id'])
            repository = None
            try:
                repository = Repository.objects.get(id=int(request.POST['id']))
            except Repository.DoesNotExist:
                pass

            if repository is None:

                response_data['status'] = "error"
                response_data[
                    'description'] = ("We re sorry, no repository " +
                                      request.POST['id'] + " found")

            else:

                file = File.create(
                    up_file.name, new_file_name,
                    up_file.content_type, 1, repository)
                file.save()

            return JsonResponse(response_data)

        else:
            response_data['status'] = "error"
            response_data[
                'description'] = "We're sorry, but something went wrong"

            return JsonResponse(response_data)
