from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,viewsets
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.





class MenuItemView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    permission_classes=[IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    permission_classes=[IsAuthenticated]
    



class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class=BookingSerializer
   permission_classes=[IsAuthenticated]