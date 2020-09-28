from django.db import models

import uuid

notifications_type = (
	("post", "post"),
	("friend", "friend")
)

class Profile(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, null=True, blank=True)
	user_id = models.UUIDField(null=True, default=uuid.uuid4, unique=True, editable=False)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user_id)

class Friend(models.Model):
	user_id = models.CharField(max_length=255)
	to_user_id = models.ForeignKey(Profile, to_field="user_id", on_delete=models.CASCADE)
	invitation_id = models.UUIDField(null=True, default=uuid.uuid4, unique=True, editable=False)
	is_accepted = models.BooleanField(null=True)
	date = models.DateTimeField(auto_now_add=True)
	date_accepted = models.DateTimeField(null=True)

	def __str__(self):
		return str(self.user_id)

class Notification(models.Model):
	body = models.CharField(max_length=255)
	to_id = models.ForeignKey(Profile, to_field="user_id", on_delete=models.CASCADE)
	type = models.CharField(max_length=100, choices=notifications_type)
	uid = models.CharField(max_length=255)
	is_seen = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)