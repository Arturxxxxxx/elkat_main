from rest_framework import generics
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    MainBanner, Category, Product, 
    AboutUsOnMainPage, Contact, Repair, WorkShop, ImagesOnAddressAndContacts, Gallery)
from .serializers import ( 
    MainBannerSerializer, CategorySerializer, 
    ProductSerializer, AboutUsOnMainPageSerializer, 
    ContactSerializer, RepairSerializer, WorkShopSerializer, ImagesOnAddressAndContactsSerializer, GallerySerializer
)


class MainBannerListView(generics.ListAPIView):
    queryset = MainBanner.objects.all()
    serializer_class = MainBannerSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AboutUsOnMainPageView(generics.RetrieveAPIView):
    queryset = AboutUsOnMainPage.objects.all()
    serializer_class = AboutUsOnMainPageSerializer

    def get_object(self):
        return AboutUsOnMainPage.get_solo()
    


class ContactView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_object(self):
        return Contact.get_solo()



class RepairView(generics.RetrieveAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

    def get_object(self):
        return Repair.get_solo()


class WorkShopView(generics.RetrieveAPIView):
    queryset = WorkShop.objects.all()
    serializer_class = WorkShopSerializer

    def get_object(self):
        return WorkShop.get_solo()


class GalleryView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def get_object(self):
        return Gallery.get_solo()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context


class ImagesOnAddressAndContactsView(generics.RetrieveAPIView):
    queryset = ImagesOnAddressAndContacts.objects.all()
    serializer_class = ImagesOnAddressAndContactsSerializer

    def get_object(self):
        return ImagesOnAddressAndContacts.get_solo()

