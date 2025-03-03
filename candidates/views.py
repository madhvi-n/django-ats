from django.db.models import Q, Case, When, IntegerField, Value, Count, Sum

from rest_framework import permissions
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from core.views import BaseViewSet

from .serializers import CandidateSerializer, CandidateReadOnlySerializer
from .models import Candidate
import random

class CandidatePagination(PageNumberPagination):
    page_size = 24


class CandidateViewSet(BaseViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CandidatePagination
    serializer_action_classes = {
        'list': CandidateReadOnlySerializer,
        'search': CandidateReadOnlySerializer
    }

    """ API to generate test data (Only for test)"""
    @action(detail=False, url_path="generate_data")
    def generate_data(self, request):
        names = [
            "Jane Doe", "Ajay Kumar Yadav", "John Doe", "Ajay Kumar", "Ajay Yadav", "Kumar Yadav", "Ramesh Yadav", "Ajay Singh", "Alice Jones"
        ]

        Candidate.objects.all().delete()
        for name in names:
            mobile = random.randint(10**9, 10**10 - 1)
            age = random.randint(23, 35)
            email_string = name.lower().replace(" ", "")
            email = f"{email_string}{age}@example.com"
            candidate, created = Candidate.objects.get_or_create(
                name=name, age=age, gender=Candidate.GenderChoices.MALE, 
                email=email, phone_number="+91" + str(mobile)
            )
        return Response({"message", "Generated dummy data successfully"}, status=status.HTTP_200_OK)

    @action(detail=False, url_path="search")
    def search_candidates(self, request):
        query = request.query_params.get("q", "").strip()

        # Handle empty query case
        if not query:
            return Response({"results": []})

        # Handle invalid characters in query
        words = query.replace("-", " ").split()
        if not words:
            return Response({"results": []})

        # Create dynamic OR filter for search
        filters = Q()
        for word in words:
            filters |= Q(name__icontains=word)


        # Annotate relevancy score based on match words
        candidates = (
            Candidate.objects.filter(filters)
            .annotate(
                relevancy=Sum(
                    Case(
                        *[When(name__icontains=word, then=Value(1)) for word in words],  
                        default=Value(0), 
                        output_field=IntegerField()
                    )
                )
            )
            .order_by("-relevancy")
        )
        return Response(CandidateSerializer(candidates, many=True).data)