from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AngularViewHits(APIView):

    hits = 0
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = None#(permissions.IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return Response({'hits': self.hits}, status=status.HTTP_201_CREATED)


class AngularViewHit(APIView):
    hits = 0

    def post(self, request, format=None):
        AngularViewHit.hits += 1
        #serializer = SnippetSerializer(data=request.DATA)
        #if serializer.is_valid():
        #    serializer.save()
        return Response({'hits': self.hits}, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

