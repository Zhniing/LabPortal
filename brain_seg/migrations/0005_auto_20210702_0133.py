# Generated by Django 3.1.7 on 2021-07-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brain_seg', '0004_uploadimage_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
