from rest_framework.serializers import ModelSerializer
from .models import *


class PolicyholderSerializer(ModelSerializer):
	class Meta:
		model = Policyholder
		fields = "__all__"