from rest_framework import serializers

from core.models.userModels import Profile

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'
		extra_kwargs = {"password": {"write_only":True}}