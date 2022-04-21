from django.shortcuts import render
import xml.etree.ElementTree as ET
from rest_framework.views import APIView
from .serializers import FluxSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import math
import requests


class FluxDataAPIView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        link = 'https://www.lemonde.fr/rss/en_continu.xml'
        response = requests.get(link)
        xml_string = response.content
        root = ET.fromstring(xml_string)
        items = root.find('channel').findall('item')
        paginator = PageNumberPagination()
        namespace = {'media': 'http://search.yahoo.com/mrss/'}
        data = list(map(lambda i, elt: {
            'id': i + 1,
            'title': elt.find('title').text,
            'description': elt.find('description').text,
            'image': elt.find('media:content', namespace).get('url')
        }, enumerate(items)))
        result_page = paginator.paginate_queryset(data, request)
        serializer = FluxSerializer(result_page, many=True)
        return Response({
            'count': len(data),
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'results': serializer.data,
            'pages': math.ceil(len(data)/paginator.page_size)
        }, status=status.HTTP_200_OK)

