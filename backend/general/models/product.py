from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена")
    discount_price = models.FloatField(verbose_name="Цена со скидкой", null=True, blank=True)
    image = models.ImageField(upload_to="products", verbose_name="Изображение")
    
    def __str__(self):
        return f"{self.title} - {self.price}" if self.price else self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"



