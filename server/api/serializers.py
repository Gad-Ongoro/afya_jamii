from rest_framework import serializers
from .models import User, Profile, Dependant, Facility, LabTest, NurseLabTestAllocation, Booking, Invoice, Payment

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role', 'dependants', 'is_verified', 'password', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True},
            'updated_at': {'read_only': True},
            'is_verified': {'read_only': True},
            'dependants': {'read_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# Dependant Serializer
class DependantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependant
        fields = '__all__'

# Facility Serializer
class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

# LabTest Serializer
class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'

# NurseLabTestAllocation Serializer
class NurseLabTestAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseLabTestAllocation
        fields = '__all__'

# Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# Invoice Serializer
class InvoiceSerializer(serializers.ModelSerializer):
    balance_due = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = ['id', 'booking', 'amount_due', 'amount_paid', 'discount', 'nurses', 'status', 'balance_due', 'created_at', 'updated_at']

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
