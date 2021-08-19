from .serializers import UploadImageSerializer
from django.shortcuts import render
import os
from myUNet import Solver, save_image
from django.conf import settings
from django.http import JsonResponse
from .models import UploadImage
from django.views.generic import View
import json
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import re
import skimage.io as io
import numpy as np
from rest_framework.decorators import action

# Create your views here.
src_img = None
seg_img = None

class DemoViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Segment
        global src_img
        global seg_img
        # Set the path
        static_root = settings.STATICFILES_DIRS[0]
        media_root = settings.MEDIA_ROOT
        upload_image = re.search('upload.*', str(serializer.data['upload'])).group(0)
        image = os.path.join(media_root, upload_image)
        model = static_root.joinpath('model/UNet.pt')
        result_img = re.sub('\.zip', '.img', image)

        # perform the segmention
        solver = Solver(gpu_idx = 0)
        seg_img = solver.segment(image, model)
        seg_img[seg_img==1] = 10
        seg_img[seg_img==2] = 150
        seg_img[seg_img==3] = 250

        # save the result image
        save_image(seg_img, result_img)

        # src image
        src_img = os.path.join(re.sub('\.zip', '_extracted', image), 'subject-9-T1.img')
        src_img = io.imread(src_img, plugin='simpleitk')
        src_img = src_img / 1000 * 256
        src_img = src_img.astype(np.uint8)
        upload_img_x = re.sub('\.zip', '_x_upload.png', image)
        upload_img_y = re.sub('\.zip', '_y_upload.png', image)
        upload_img_z = re.sub('\.zip', '_z_upload.png', image)
        save_image(src_img[129, :, :], upload_img_x)
        save_image(src_img[::-1, 97, :], upload_img_y)
        save_image(src_img[::-1, :, 73], upload_img_z)

        # 129, 97, 73
        result_img_x = re.sub('\.zip', '_x.png', image)
        result_img_y = re.sub('\.zip', '_y.png', image)
        result_img_z = re.sub('\.zip', '_z.png', image)
        save_image(seg_img[129, :, :], result_img_x)
        save_image(seg_img[::-1, 97, :], result_img_y)
        save_image(seg_img[::-1, :, 73], result_img_z)
        # tnemgeS

        # Update the UploadImage object
        upload_img = UploadImage.objects.get(upload=upload_image)
        upload_img.result_img = re.search('upload.*', result_img).group(0)
        result_name = upload_img.result_img.name
        upload_img.image_name = image
        upload_img.result_hdr = re.sub('\.img', '.hdr', result_name)
        upload_img.upload_img_x = re.sub('\.img', '_x_upload.png', result_name)
        upload_img.upload_img_y = re.sub('\.img', '_y_upload.png', result_name)
        upload_img.upload_img_z = re.sub('\.img', '_z_upload.png', result_name)
        upload_img.result_img_x = re.sub('\.img', '_x.png', result_name)
        upload_img.result_img_y = re.sub('\.img', '_y.png', result_name)
        upload_img.result_img_z = re.sub('\.img', '_z.png', result_name)
        upload_img.save()

        serializer = UploadImageSerializer(upload_img, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # return super().create(request, *args, **kwargs)

    @action(methods=['post'], detail=False, url_path='set_x')
    def set_x(self, request):
        image = request.data['img']
        src_img = os.path.join(re.sub('\.zip', '_extracted', image), 'subject-9-T1.img')
        result_img = re.sub('\.zip', '.img', image)

        src_img = io.imread(src_img, plugin='simpleitk')
        src_img = src_img / 1000 * 256
        src_img = src_img.astype(np.uint8)
        result_img = io.imread(result_img, plugin='simpleitk')
        result_img = result_img.astype(np.uint8)

        x = request.data['x']
        upload_img_x = re.sub('\.zip', '_x_upload.png', image)
        result_img_x = re.sub('\.zip', '_x.png', image)
        save_image(src_img[x, :, :], upload_img_x)
        save_image(result_img[x, :, :], result_img_x)

        upload_img = UploadImage.objects.get(upload=re.search('upload.*', image).group(0))
        serializer = UploadImageSerializer(upload_img, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['post'], detail=False, url_path='set_y')
    def set_y(self, request):
        image = request.data['img']
        src_img = os.path.join(re.sub('\.zip', '_extracted', image), 'subject-9-T1.img')
        result_img = re.sub('\.zip', '.img', image)

        src_img = io.imread(src_img, plugin='simpleitk')
        src_img = src_img / 1000 * 256
        src_img = src_img.astype(np.uint8)
        result_img = io.imread(result_img, plugin='simpleitk')
        result_img = result_img.astype(np.uint8)

        y = request.data['y']
        upload_img_y = re.sub('\.zip', '_y_upload.png', image)
        result_img_y = re.sub('\.zip', '_y.png', image)
        save_image(src_img[::-1, y, :], upload_img_y)
        save_image(result_img[::-1, y, :], result_img_y)

        upload_img = UploadImage.objects.get(upload=re.search('upload.*', image).group(0))
        serializer = UploadImageSerializer(upload_img, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['post'], detail=False, url_path='set_z')
    def set_z(self, request):
        image = request.data['img']
        src_img = os.path.join(re.sub('\.zip', '_extracted', image), 'subject-9-T1.img')
        result_img = re.sub('\.zip', '.img', image)

        src_img = io.imread(src_img, plugin='simpleitk')
        src_img = src_img / 1000 * 256
        src_img = src_img.astype(np.uint8)
        result_img = io.imread(result_img, plugin='simpleitk')
        result_img = result_img.astype(np.uint8)

        z = request.data['z']
        upload_img_z = re.sub('\.zip', '_z_upload.png', image)
        result_img_z = re.sub('\.zip', '_z.png', image)
        save_image(src_img[::-1, :, z], upload_img_z)
        save_image(result_img[::-1, :, z], result_img_z)

        upload_img = UploadImage.objects.get(upload=re.search('upload.*', image).group(0))
        serializer = UploadImageSerializer(upload_img, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TestView(View):

    def post(self, request):
        # data = request.body.decode()
        # data_dict = json.load(data)

        data_dict = {}
        # data_dict = JSONParser().parse(request)

        data_dict['upload'] = request.FILES.get('upload')

        # seri = UploadImageSerializer(data=data_dict)
        # seri.is_valid(raise_exception=True)  # 自动返回响应

        return JsonResponse({"re": "ok"})


def demo(request):
    if request.method == 'GET':

        return render(request, 'brain_seg/demo.html')

    if request.method == 'POST':
        # dic = {}
        media_root = settings.MEDIA_ROOT
        static_root = settings.STATICFILES_DIRS[0]

        # Save image file
        upload_file = request.FILES.get('img')
        # uploaded_file.save()
        img = UploadImage.objects.create(upload_image=upload_file)
        filename = img.get_file_name()

        # img_path = os.path.join('images', uploaded_file.name)
        # # dic["img_path"] = img_path
        # with open(static_dir.joinpath(img_path), 'wb') as f:
        #     for chunk in uploaded_file.chunks():
        #         f.write(chunk)

        # Segmentation
        # uploaded_file_base_name = os.path.splitext(upload_file.name)[0]
        file_base_name = os.path.splitext(filename)[0]
        model_name = static_root.joinpath('model/UNet.pt')
        result_dir = media_root.joinpath('result', file_base_name)
        zip_name = media_root.joinpath(str(img.img))
        solver = Solver(gpu_idx=1)

        seg_img = solver.segment(zip_name, model_name)

        if not os.path.isdir(result_dir):
            os.mkdir(result_dir)
        seg_img_name = os.path.join(result_dir, file_base_name + '.img')
        save_image(seg_img, seg_img_name)

        # dic['data'] = seg_img.tolist()

        # return JsonResponse({'seg_img': seg_img.tolist()})
        return JsonResponse({'result': 1, 'file_name': filename, 'seg_img_name': seg_img_name})
        # return HttpResponse("hello upload")


def get_slice(request):
    if request.method == 'POST':

        return JsonResponse({'x': '1', 'y': '2', 'z': '3'})
