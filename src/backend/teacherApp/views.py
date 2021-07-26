from rest_framework import viewsets


from .serializers import *


# Create your views here.
class BackendAccountView(viewsets.ModelViewSet):
    queryset = BackendAccount.objects.all()
    serializer_class = BackendAccountSerializer
