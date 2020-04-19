from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import MetaData, Document
from .serializers import MetaDataSerializer, DocumentSerializer


class MetaDataListCreateAPIView(ListCreateAPIView):
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer


class MetaDataRetrieveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer


class DocumentListCreateAPIView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentRetrieveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
