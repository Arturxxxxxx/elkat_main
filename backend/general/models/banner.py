from django.db import models
from solo.models import SingletonModel


class MainBanner(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="banners", verbose_name="Изображение")


    def __str__(self):
        return self.image.url
        
    
    class Meta:
        verbose_name = "Главный баннер"
        verbose_name_plural = "Главный баннер"
    



