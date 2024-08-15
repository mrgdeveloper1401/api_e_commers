from rest_framework.urls import path
from images.views import DetailsImageView, ListImagesView


app_name = 'image'
urlpatterns = [
    path('image/<int:pk>/', DetailsImageView.as_view(), name='details_image'),
    # path('image_list/', ListImagesView.as_view(), name='list_image'),
]