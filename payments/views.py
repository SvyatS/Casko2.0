from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


def Homepage(request):
	drivers = Policyholder.objects.all()
	return render(request, "homepage.html", {"drivers": drivers})

def CreatePayment(request):
	return render(request, "createDriver.html")


class PolicyholderViewSet(ModelViewSet):
	queryset = Policyholder.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = PolicyholderSerializer

