from django.urls import path
from .views import (
    LocationListCreateView, LocationRetrieveUpdateDestroyView,
    MemberListCreateView, MemberRetrieveUpdateDestroyView,
    DependantListCreateView, DependantRetrieveUpdateDestroyView,
    LabTestListCreateView, LabTestRetrieveUpdateDestroyView,
    NurseListCreateView, NurseRetrieveUpdateDestroyView,
    NurseLabTestAllocationListCreateView, NurseLabTestAllocationRetrieveUpdateDestroyView,
    PaymentListCreateView, PaymentRetrieveUpdateDestroyView,
    BookingListCreateView, BookingRetrieveUpdateDestroyView
)

urlpatterns = [
    # Location URLs
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<uuid:pk>/', LocationRetrieveUpdateDestroyView.as_view(), name='location-retrieve-update-destroy'),
    
    # Member URLs
    path('members/', MemberListCreateView.as_view(), name='member-list-create'),
    path('members/<uuid:pk>/', MemberRetrieveUpdateDestroyView.as_view(), name='member-retrieve-update-destroy'),
    
    # Dependant URLs
    path('dependants/', DependantListCreateView.as_view(), name='dependant-list-create'),
    path('dependants/<uuid:pk>/', DependantRetrieveUpdateDestroyView.as_view(), name='dependant-retrieve-update-destroy'),
    
    # LabTest URLs
    path('labtests/', LabTestListCreateView.as_view(), name='labtest-list-create'),
    path('labtests/<uuid:pk>/', LabTestRetrieveUpdateDestroyView.as_view(), name='labtest-retrieve-update-destroy'),
    
    # Nurse URLs
    path('nurses/', NurseListCreateView.as_view(), name='nurse-list-create'),
    path('nurses/<uuid:pk>/', NurseRetrieveUpdateDestroyView.as_view(), name='nurse-retrieve-update-destroy'),
    
    # NurseLabTestAllocation URLs
    path('nurse-labtest-allocations/', NurseLabTestAllocationListCreateView.as_view(), name='nurse-labtest-allocation-list-create'),
    path('nurse-labtest-allocations/<uuid:pk>/', NurseLabTestAllocationRetrieveUpdateDestroyView.as_view(), name='nurse-labtest-allocation-retrieve-update-destroy'),
    
    # Payment URLs
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<uuid:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-retrieve-update-destroy'),
    
    # Booking URLs
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<uuid:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-retrieve-update-destroy'),
]