
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NoPagination():

    def get_response(self, data):
        return Response({
            'count': data.count,
            'next': 1,
            'current': 1,
            'previous': 1,
            'num_pages': 1,
            'links': {
                'next': 1,
                'previous': 1
            },
            'results': data,
            'page_size': data.count

        })


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_number(),
            'current': self.page.number,
            'previous': self.get_previous_number(),
            'num_pages': (self.page.paginator.count // self.page_size),
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'results': data,
            'page_size': self.page_size,

        })

    def get_next_number(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_previous_number(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()

        return page_number


class LargeResultsSetPagination(StandardResultsSetPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000
