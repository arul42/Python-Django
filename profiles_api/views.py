from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of API Views"""
        an_apiview = [
        'uses methods (Get, Put, Post, Patch, delete)',
        'similarly like django traditional views',
        'gives you most control over the application',
        'Is mapped manulay to the url',
        ]

        return Response({'message':'Hello World', 'an_apiview': an_apiview})

    def post(self, request):
        """Create Hello message with our names"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Updating all the content"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Update only partial contents"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete content"""
        return Response({'message': 'DELETE'})
            
