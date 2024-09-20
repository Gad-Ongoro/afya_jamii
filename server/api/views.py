from rest_framework import generics
from .models import User, Profile, Dependant, Facility, LabTest, NurseLabTestAllocation, Booking, Invoice, Payment
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    DependantSerializer,
    FacilitySerializer,
    LabTestSerializer,
    NurseLabTestAllocationSerializer,
    BookingSerializer,
    InvoiceSerializer,
    PaymentSerializer
)

# Normal User Signup View
class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(role='member')

# Nurse Signup View
class NurseSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(role='nurse')

# Doctor Signup View
class DoctorSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(role='doctor')
   
# Users list
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Detail View
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Profile Views
class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Dependant Views
class DependantListCreateView(generics.ListCreateAPIView):
    queryset = Dependant.objects.all()
    serializer_class = DependantSerializer

class DependantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dependant.objects.all()
    serializer_class = DependantSerializer

# Facility Views
class FacilityListCreateView(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class FacilityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

# LabTest Views
class LabTestListCreateView(generics.ListCreateAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

class LabTestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

# NurseLabTestAllocation Views
class NurseLabTestAllocationListCreateView(generics.ListCreateAPIView):
    queryset = NurseLabTestAllocation.objects.all()
    serializer_class = NurseLabTestAllocationSerializer

class NurseLabTestAllocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NurseLabTestAllocation.objects.all()
    serializer_class = NurseLabTestAllocationSerializer

# Booking Views
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Invoice Views
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# Payment Views
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
