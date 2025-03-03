from rest_framework import serializers
from candidates.models import Candidate



class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ("id", "name", "gender", "age", "email", "phone_number")
        read_only_fields  = ("id", )



class CandidateReadOnlySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    gender = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    phone_number = serializers.CharField(read_only=True)