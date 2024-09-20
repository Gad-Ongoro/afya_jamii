from django.urls import path
from .views import (
    UserSignupView, NurseSignupView, DoctorSignupView, UserListView, UserRetrieveUpdateDestroyView,
    ProfileListView, ProfileRetrieveUpdateDestroyView,
    DependantListCreateView, DependantRetrieveUpdateDestroyView,
    FacilityListCreateView, FacilityRetrieveUpdateDestroyView,
    LabTestListCreateView, LabTestRetrieveUpdateDestroyView,
    NurseLabTestAllocationListCreateView, NurseLabTestAllocationRetrieveUpdateDestroyView,
    BookingListCreateView, BookingRetrieveUpdateDestroyView,
    InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView,
    PaymentListCreateView, PaymentRetrieveUpdateDestroyView
)

urlpatterns = [
    # User
    path('register/user/', UserSignupView.as_view(), name='user-signup'),
    path('register/nurse/', NurseSignupView.as_view(), name='nurse-signup'),
    path('register/doctor/', DoctorSignupView.as_view(), name='doctor-signup'),
    path('users/', UserListView.as_view(), name='users-list'),
    path('users/<uuid:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),

    # Profile
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<uuid:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),

    # Dependant
    path('dependants/', DependantListCreateView.as_view(), name='dependant-list-create'),
    path('dependants/<uuid:pk>/', DependantRetrieveUpdateDestroyView.as_view(), name='dependant-detail'),

    # Facility
    path('facilities/', FacilityListCreateView.as_view(), name='facility-list-create'),
    path('facilities/<uuid:pk>/', FacilityRetrieveUpdateDestroyView.as_view(), name='facility-detail'),

    # LabTest
    path('labtests/', LabTestListCreateView.as_view(), name='labtest-list-create'),
    path('labtests/<uuid:pk>/', LabTestRetrieveUpdateDestroyView.as_view(), name='labtest-detail'),

    # NurseLabTestAllocation
    path('nurse-labtest-allocations/', NurseLabTestAllocationListCreateView.as_view(), name='nurse-labtest-allocation-list-create'),
    path('nurse-labtest-allocations/<uuid:pk>/', NurseLabTestAllocationRetrieveUpdateDestroyView.as_view(), name='nurse-labtest-allocation-detail'),

    # Booking
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<uuid:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-detail'),

    # Invoice
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<uuid:pk>/', InvoiceRetrieveUpdateDestroyView.as_view(), name='invoice-detail'),

    # Payment
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<uuid:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail'),
]