from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop


latitude =  28.5626728
longitude = 89.2244577

user_location = Point(longitude, latitude, srid=4326)
# Create your views here.
class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:2]
    template_name = "shops/index.html"
