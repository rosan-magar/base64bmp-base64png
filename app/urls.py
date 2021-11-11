from django.contrib import admin
from django.urls import path
from rest_framework import routers, urlpatterns
from .views import UploadImage
from django.urls import include

router=routers.DefaultRouter()
# router.register('upload-image', UploadImage.as_view())

urlpatterns = [
    path("", include(router.urls)),
    path("upload-image", UploadImage.as_view())
    # path("convert-base64-bmp-to-base64-png", UploadImage.as_view())

]