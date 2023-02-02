from datetime import datetime
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView ,RetrieveUpdateAPIView ,DestroyAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer,BookingDetailsSerializers,BookingUpdateSerializer,BookingDeleteSerializers


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailsSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class BookingUpdateView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    # becouse its delete we don't need to pass data
    # so we can use any serializer
    serializer_class = BookingDetailView 