from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to="categories", verbose_name="Изображение")

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталог"

    def __str__(self):
        return self.title
