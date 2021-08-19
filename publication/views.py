from rest_framework import viewsets, views
from django.views.generic import View
from .models import Author, Paper, Image
from .serializers import AuthorSerializer, PaperSerializer, ImageSerializer, PaperBriefSerializer
from django.http.response import JsonResponse

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class HomeView(View):

    def get(self, request):
        image_qs = Image.objects.filter(display_in_home=True)
        image_seri = ImageSerializer(image_qs, context={'request': request}, many=True)
        paper_qs = Paper.objects.all()
        paper_seri = PaperBriefSerializer(paper_qs, context={'request': request}, many=True)

        return JsonResponse({
            'images': image_seri.data,
            'researchfield': '小样本学习，行人重识别，多姿态人脸识别，单样本人脸识别，医学图像分割',
            'papers': paper_seri.data
        }, safe=False)
