from django.db import models
import re


class UploadImage(models.Model):
    upload = models.FileField(upload_to='upload')
    image_name = models.CharField(max_length=100, blank=True)

    # upload_x_hdr = models.FileField(blank=True)
    upload_img_x = models.FileField(blank=True)
    # upload_y_hdr = models.FileField(blank=True)
    upload_img_y = models.FileField(blank=True)
    # upload_z_hdr = models.FileField(blank=True)
    upload_img_z = models.FileField(blank=True)

    result_hdr = models.FileField(blank=True)
    result_img = models.FileField(blank=True)
    
    # result_x_hdr = models.FileField(blank=True)
    result_img_x = models.FileField(blank=True)
    # result_y_hdr = models.FileField(blank=True)
    result_img_y = models.FileField(blank=True)
    # result_z_hdr = models.FileField(blank=True)
    result_img_z = models.FileField(blank=True)

    class Meta:
        db_table = 'upload_images'
        verbose_name = '上传的图片'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.upload_image.name

    def delete(self):
        super().delete()
        for attr in vars(self):
            if re.match('(^upload)|(^result)', attr):
                getattr(self, attr).delete()
