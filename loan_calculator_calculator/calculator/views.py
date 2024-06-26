from django.shortcuts import render

from rest_framework import generics

from .models import Loan
from .serializers import LoanSerializer


# Create your views here.
class LoanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
