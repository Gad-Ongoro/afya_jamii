from rest_framework import generics
from .models import Member, Location, Dependant, LabTest, Nurse, NurseLabTestAllocation, Payment, Booking
from .serializers import MemberSerializer, LocationSerializer, DependantSerializer, LabTestSerializer, NurseSerializer, NurseLabTestAllocationSerializer, PaymentSerializer, BookingSerializer

# Location Views
class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Member Views
class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Dependant Views
class DependantListCreateView(generics.ListCreateAPIView):
    queryset = Dependant.objects.all()
    serializer_class = DependantSerializer

class DependantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependant.objects.all()
    serializer_class = DependantSerializer

# LabTest Views
class LabTestListCreateView(generics.ListCreateAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

class LabTestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

# Nurse Views
class NurseListCreateView(generics.ListCreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class NurseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

# NurseLabTestAllocation Views
class NurseLabTestAllocationListCreateView(generics.ListCreateAPIView):
    queryset = NurseLabTestAllocation.objects.all()
    serializer_class = NurseLabTestAllocationSerializer

class NurseLabTestAllocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NurseLabTestAllocation.objects.all()
    serializer_class = NurseLabTestAllocationSerializer

# Payment Views
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# Booking Views
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
