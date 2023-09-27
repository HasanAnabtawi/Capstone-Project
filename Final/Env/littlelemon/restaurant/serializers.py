from django.contrib.auth.models import User
from .models import Menu,Booking
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
     

     class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']


class BookingSerializer(serializers.ModelSerializer):
     

     class Meta:
        model = Booking
        fields = ['id', 'Name', 'No_of_guests', 'BookingDate']