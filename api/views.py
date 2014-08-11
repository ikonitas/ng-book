from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, views
from .serializers import UserSerializer, GroupSerializer


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

class AngularView(views.APIView):

    def get(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        return self.retrieve(request, *args, **kwargs)


    def post(self, request, format=None):
        import ipdb; ipdb.set_trace()
        #serializer = SnippetSerializer(data=request.DATA)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.http import HttpResponse


def drakonas(request):
    return HttpResponse("boom")
