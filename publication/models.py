from django.db import models
from datetime import date

# Create your models here.

class Author(models.Model):
    # id = models.IntegerField('ID', primary_key=True)
    name = models.CharField('姓名', max_length=10)
    English_name = models.CharField('英文名', max_length=30)
    portrait = models.ImageField('头像', upload_to='portrait', blank=True)
    email = models.EmailField('邮箱', blank=True)
    grade = models.IntegerField('入学年份(0代表老师)')
    introduction = models.TextField('介绍', blank=True)
    researchfield = models.TextField('研究方向', blank=True)
    # achievement = models.TextField('成果', blank=True)

    class Meta:
        db_table = 'authors'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name


class Paper(models.Model):
    # id = models.AutoField('ID', primary_key=True)
    title = models.CharField('标题', max_length=40)
    authors = models.ManyToManyField(Author, related_name='papers', verbose_name='作者')
    publisher = models.CharField('出版商', max_length=40, blank=True)
    date = models.DateField('见刊日期', default=date.today, blank=True)
    abstract = models.TextField('摘要')
    paper_link = models.URLField('论文链接', blank=True)
    paper_pdf = models.FileField('论文pdf', upload_to='papers', blank=True)
    code_link = models.URLField('代码链接', blank=True)

    class Meta:
        db_table = 'papers'
        verbose_name = '论文'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    # id = models.IntegerField('ID', primary_key=True)
    image = models.ImageField('图片', upload_to='images')
    # on_delete=models.CASCADE -> 删除论文时，同时删除关联的图片
    paper = models.ForeignKey(Paper, related_name='images', on_delete=models.CASCADE, verbose_name='所属论文')
    illustration = models.TextField('说明', blank=True)
    display_in_home = models.BooleanField('首页展示', default=False)

    class Meta:
        db_table = 'images'
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image.name

    def delete(self):
        super().delete()
        # self.url.storage.delete(self.url.name)  # 同时删除文件
        self.image.delete()
