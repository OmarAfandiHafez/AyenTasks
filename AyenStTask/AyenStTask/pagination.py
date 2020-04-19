from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 48

    def get_page_count(self, items_count, page_size):
        if items_count <= page_size:
            return 1
        elif items_count % page_size == 0:
            return int(items_count / page_size)
        else:
            return int(items_count / page_size) + 1

    def get_paginated_response(self, data):
        page_size = self.page_size
        if 'page_size' in self.request.query_params:
            if self.request.query_params['page_size'].isnumeric():
                if int(self.request.query_params['page_size']) > 0:
                    page_size = int(self.request.query_params['page_size'])
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'pages_count': self.get_page_count(self.page.paginator.count, page_size),
            'results': data
        })
