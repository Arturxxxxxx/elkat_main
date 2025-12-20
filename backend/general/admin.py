from django.contrib import admin
from .models import (MainBanner, Category, Product, 
    AboutUsOnMainPage, Contact, Repair, WorkShop, ImagesOnAddressAndContacts, Gallery, GalleryImage
)

admin.site.site_header = 'Администрация Эклат'
admin.site.site_title = 'Администрация Эклат'

@admin.register(MainBanner)
class MainBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price')
    search_fields = ('title',)


@admin.register(AboutUsOnMainPage)
class AboutUsOnMainPageAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone',)

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(WorkShop)
class WorkShopAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ImagesOnAddressAndContacts)
class ImagesOnAddressAndContactsAdmin(admin.ModelAdmin):
    list_display = ('address_image',)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
    list_display = ('id',)
    inlines = [GalleryImageInline]

