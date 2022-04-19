from django.shortcuts import render
import xml.etree.ElementTree as ET
from rest_framework.views import APIView
from .serializers import FluxSerializer
from rest_framework.response import Response
from rest_framework import status
import requests


class FluxDataAPIView(APIView):
    def get(self, request):
        link = 'https://www.lemonde.fr/rss/en_continu.xml'
        response = requests.get(link)
        xml_string = response.content
        root = ET.fromstring(xml_string)
        items = root.find('channel').findall('item')

        data = list(map(lambda item: {
            'title': item.find('title').text,
            'description': item.find('description').text,
            'image': item.find('media:content')
        }, items))

        serializer = FluxSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
