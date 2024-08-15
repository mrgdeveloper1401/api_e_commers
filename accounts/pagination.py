from rest_framework.pagination import PageNumberPagination


class PublicNotificationPagination(PageNumberPagination):
    page_size = 10
