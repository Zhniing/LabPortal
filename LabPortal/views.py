# from LabPortal.settings import STATICFILES_DIRS
from django.conf import settings
from django.shortcuts import render
import os
import numpy as np
from django.http import JsonResponse


def index(request):
    return render(request, 'brain_seg/demo.html')


def result(request):
    if request.method == 'GET':
        a = np.zeros(27).reshape(3,3,3)
        a[0, 0, 0] = 3
        a[1, 1, 1] = 3
        a[2, 2, 2] = 3
        dic = {'a': a.tolist()}
        return render(request, 'test.html', dic)


def upload(request):
    dic = {}
    media_dir = settings.MEDIA_ROOT

    # Save image file
    uploaded_file = request.FILES.get('img')
    img_path = os.path.join('upload', uploaded_file.name)
    dic["img_path"] = img_path
    with open(media_dir.joinpath(img_path), 'wb') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)

    return JsonResponse({'result': 1, 'b': 2})