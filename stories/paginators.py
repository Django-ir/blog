from rest_framework import pagination


class LimitPostsPaginator(pagination.PageNumberPagination):
    page_size = 5
