from django.db.models import fields
from rest_framework import serializers
from .models import Paper, Test


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper  # 指定生成字段的模型类
        fields = '__all__'  # 指定所需字段
        # exclude = ()  # 取反


# 自定义序列化器
class TestSerializer(serializers.Serializer):

    # 序列化返回字段
    name = serializers.CharField()  # 变量名必须跟model中的一致
