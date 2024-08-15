from rest_framework.generics import RetrieveAPIView, ListAPIView

from images.models import Image
from images.serialziers import ImageSerializer


class DetailsImageView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ListImagesView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
