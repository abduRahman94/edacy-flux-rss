from django.shortcuts import render
from requests_xml import XMLSession()
# Create your views here.


def get_flux(request):
    session = XMLSession()
    link = 'https://www.lemonde.fr/rss/en_continu.xml'
    response = session.get(link)
    links = response.xml.links
    return render(request, 'flux/test_flux.html', context={'data': links})
