from django.urls import path
from .views import (
    MainBannerListView, CategoryListView, ProductListView,
    AboutUsOnMainPageView, ContactView, RepairView, WorkShopView, ImagesOnAddressAndContactsView, GalleryView
)

urlpatterns = [
    path('main-banner/', MainBannerListView.as_view(), name='main-banner-list'),
    path('catalog/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('about-us/', AboutUsOnMainPageView.as_view(), name='about-us-on-main-page-list'),
    path('contact/', ContactView.as_view(), name='contact-list'),
    path('repair/', RepairView.as_view(), name='repair'),
    path('workshop/', WorkShopView.as_view(), name='workshop'),
    path('images-on-bottom/', ImagesOnAddressAndContactsView.as_view(), name='images-on-address'),
    path('gallery/', GalleryView.as_view(), name='gallery'),

]
