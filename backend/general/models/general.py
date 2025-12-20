from django.db import models
from solo.models import SingletonModel

class AboutUsOnMainPage(SingletonModel):
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Repair(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    description2 = models.TextField(verbose_name="Описание2")
    image = models.ImageField(upload_to="repair", verbose_name="Изображение")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ремонт кресел"
        verbose_name_plural = "Ремонт кресел"


class WorkShop(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    description2 = models.TextField(verbose_name="Описание2")
    description3 = models.TextField(verbose_name="Описание3")
    description4 = models.TextField(verbose_name="Описание4")
    image = models.ImageField(upload_to="workshop", verbose_name="Фоновое изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мастерская"
        verbose_name_plural = "Мастерская"


class Contact(SingletonModel):
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    work_time = models.CharField(max_length=255, verbose_name="Время работы")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    instagram = models.URLField(verbose_name="Instagram")
    telegram = models.URLField(verbose_name="Telegram")
    whatsapp = models.CharField(max_length=255, verbose_name="WhatsApp")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

class ImagesOnAddressAndContacts(SingletonModel):
    address_image = models.ImageField(upload_to="images_on_address", verbose_name="Изображение в адресе")
    contact_image = models.ImageField(upload_to="images_on_address", verbose_name="Изображение в контактах")

    class Meta:
        verbose_name = "Изображения снизу главной страницы"
        verbose_name_plural = "Изображения снизу главной страницы"

class Gallery(SingletonModel):

    def __str__(self):
        return "Галерея"

    class Meta:
        verbose_name = "Галерею"
        verbose_name_plural = "Галерея"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery", verbose_name="Изображение")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name="Изображения")

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"
