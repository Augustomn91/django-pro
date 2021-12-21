from rest_framework import pagination


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 3
    limit_query_param = '1'
    offset_query_param = '0'
    max_limit = 50
