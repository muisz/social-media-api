from django.db import models

from .userModels import Profile

import uuid

class Post(models.Model):
	user_id = models.ForeignKey(Profile, to_field="user_id", on_delete=models.CASCADE)
	post_id = models.UUIDField(default=uuid.uuid4, null=True, unique=True, editable=False)
	body = models.TextField()
	tags = models.TextField(null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_edited = models.DateTimeField(null=True)

	def __str__(self):
		return str(self.post_id)

class Comment(models.Model):
	comment_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
	to_post_id = models.ForeignKey(Post, to_field="post_id", on_delete=models.CASCADE, null=True)
	user_id = models.ForeignKey(Profile, to_field="user_id", on_delete=models.CASCADE, blank=True)
	to_comment_id = models.ForeignKey("self", to_field="comment_id", on_delete=models.CASCADE, null=True)
	body = models.TextField()
	date_edited = models.DateTimeField(auto_now_add=True)
	date_edited = models.DateTimeField(null=True)

	def __str__(self):
		return str(self.comment_id)

class Tag(models.Model):
	post_id = models.ForeignKey(Post, to_field="post_id", on_delete=models.CASCADE)
	tag = models.CharField(max_length=255)