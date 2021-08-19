from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=20)
    test = models.CharField(max_length=20, null=True)


class Paper(models.Model):
    title = models.CharField('标题', max_length=40)
    authors = models.CharField('作者', max_length=40)
    abstract = models.TextField('摘要')
    paper_link = models.CharField('论文链接', max_length=100)
    code_link = models.CharField('代码链接', max_length=100)

    class Meta:
        db_table = 'paper_t'
        verbose_name = '论文'
        verbose_name_plural =verbose_name

    def __str__(self) -> str:
        return self.title


class Test(models.Model):
    choices = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'test'

    def __str__(self) -> str:
        return self.name
