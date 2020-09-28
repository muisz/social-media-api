from django.db import models

import uuid

class Profile(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, null=True, blank=True)
	user_id = models.UUIDField(null=True, default=uuid.uuid4, unique=True, editable=False)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user_id)