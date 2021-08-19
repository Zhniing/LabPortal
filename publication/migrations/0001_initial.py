# Generated by Django 3.1.7 on 2021-06-30 12:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('English_name', models.CharField(max_length=30, verbose_name='英文名')),
                ('portrait', models.ImageField(blank=True, upload_to='portrait', verbose_name='头像')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='邮箱')),
                ('grade', models.IntegerField(verbose_name='入学年份(0代表老师)')),
                ('introduction', models.TextField(blank=True, verbose_name='介绍')),
                ('researchfield', models.TextField(blank=True, verbose_name='研究方向')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='标题')),
                ('publisher', models.CharField(blank=True, max_length=40, verbose_name='出版商')),
                ('date', models.DateField(blank=True, default=datetime.date.today, verbose_name='见刊日期')),
                ('abstract', models.TextField(verbose_name='摘要')),
                ('paper_link', models.URLField(blank=True, verbose_name='论文链接')),
                ('paper_pdf', models.FileField(blank=True, upload_to='papers', verbose_name='论文pdf')),
                ('code_link', models.URLField(blank=True, verbose_name='代码链接')),
                ('authors', models.ManyToManyField(related_name='papers', to='publication.Author', verbose_name='作者')),
            ],
            options={
                'verbose_name': '论文',
                'verbose_name_plural': '论文',
                'db_table': 'papers',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='图片')),
                ('illustration', models.TextField(blank=True, verbose_name='说明')),
                ('display_in_home', models.BooleanField(default=False, verbose_name='首页展示')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='publication.paper', verbose_name='所属论文')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
                'db_table': 'images',
            },
        ),
    ]
