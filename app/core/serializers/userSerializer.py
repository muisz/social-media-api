from rest_framework import serializers

from core.models.userModels import Profile, Friend, Notification

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'
		extra_kwargs = {"password": {"write_only":True}}

class FriendSerializer(serializers.ModelSerializer):
	class Meta:
		model = Friend
		fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = '__all__'