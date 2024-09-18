from rest_framework import serializers
from .models import Member, Location, Dependant, LabTest, Nurse, NurseLabTestAllocation, Payment, Booking

# Location Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

# Member Serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'phone', 'dob', 'location', 'password', 'date_joined']
        # extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        return Member.objects.create_user(**validated_data)

# Dependant Serializer
class DependantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependant
        fields = ['id', 'member', 'surname', 'others', 'dob', 'reg_date']

# LabTest Serializer
class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = ['id', 'test_name', 'test_description', 'test_cost', 'test_discount', 'availability', 'more_info', 'reg_date']

# Nurse Serializer
class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['id', 'surname', 'gender', 'email', 'phone', 'password', 'reg_date']

# NurseLabTestAllocation Serializer
class NurseLabTestAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseLabTestAllocation
        fields = ['id', 'nurse', 'invoice_no', 'flag', 'reg_date']

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'invoice_no', 'total_amount', 'new_field', 'reg_date']

# Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'member', 'booked_for', 'dependant', 'test', 'appointment_date', 'appointment_time', 'where_taken', 'latitude']
