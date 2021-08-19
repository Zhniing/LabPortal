from rest_framework import serializers
from .models import Author, Paper, Image


class AuthorBriefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'English_name')


class ImageBriefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class PaperBriefSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorBriefSerializer(many=True, read_only=True)
    images = ImageBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Paper
        fields = ('url', 'id', 'title', 'authors', 'paper_link', 'paper_pdf', 'code_link', 'images')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    # 看看底层怎么实现的
    papers = PaperBriefSerializer(many=True, read_only=True)  # nested

    class Meta:
        model = Author
        fields = '__all__'


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    images = ImageBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Paper
        fields = '__all__'


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    paper = PaperSerializer(read_only=True)

    class Meta:
        model = Image
        fields = ('image', 'paper')

