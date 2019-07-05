from rest_framework import pagination, response


class CustomPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return response.Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'results': data
        })
