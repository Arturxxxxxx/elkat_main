from rest_framework import serializers

from general.models import MainBanner, Category, Product, AboutUsOnMainPage, Contact, Repair, WorkShop, ImagesOnAddressAndContacts, Gallery, GalleryImage



class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AboutUsOnMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsOnMainPage
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
 

class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = '__all__'

class WorkShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkShop
        fields = '__all__'

class ImagesOnAddressAndContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesOnAddressAndContacts
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images_list = []
        gallery_images = GalleryImage.objects.all()
        for image in gallery_images:
            images_list.append(self.context['request'].build_absolute_uri(image.image.url))
        return images_list
    
    class Meta:
        model = Gallery
        fields = ('images',)