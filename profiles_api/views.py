from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Return a list of API Views"""
        an_apiview = [
        'uses methods (Get, Put, Post, Patch, delete)',
        'similarly like django traditional views',
        'gives you most control over the application',
        'Is mapped manulay to the url',
        ]

        return Response({'message':'Hello World', 'an_apiview': an_apiview})
