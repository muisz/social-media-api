from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView

from app.utils import BadRequestResponse, AssertionErrorResponse

from core.models.postModels import Post, Comment, Tag
from core.models.userModels import Profile
from core.serializers.postSerializer import PostSerializer, CommentSerializer
from core.serializers.userSerializer import ProfileSerializer
from core.tools.encryptions import set_password, verify_password

API_VERSION = settings.API_VERSION

class PostView(APIView):
	def post(self, request, versions):
		try:
			assert versions in API_VERSION, "version not found"
			if versions == 'v1':
				data = request.data
				serializer = PostSerializer(data = data)
				if serializer.is_valid():
					saved = serializer.save()
					list_tag = data.get('tags').split(',')
					print(list_tag)
					for tag in list_tag:
						Tag.objects.create(post_id = saved, tag = tag)
					return Response({"data":PostSerializer(saved).data})

				else:
					raise

		except AssertionError as error:
			return AssertionErrorResponse({"msg":error.__str__()}, 400)

		except:
			return BadRequestResponse({"msg":"Bad Request"})

	def get(self, request, versions):
		try:
			assert versions in API_VERSION, "version not found"
			if versions == 'v1':
				post = Post.objects.all()
				if 'tag' in request.GET and request.GET['tag'] != '':
					tags = Tag.objects.filter(tag = request.GET['tag'])
					post = []
					for tag in tags:
						post.append(tag.post_id)
					print(post)
				data = PostSerializer(post, many=True).data
				return Response({"data":data})

		except AssertionError as error:
			return AssertionErrorResponse({"msg":error.__str__()}, 404)

class PostDetail(APIView):
	def get(self, request, versions, post_id):
		try:
			assert versions in API_VERSION, "version not found"
			if versions == 'v1':
				post = Post.objects.get(post_id = post_id)
				comments = Comment.objects.filter(to_post_id = post, to_comment_id = None)
				# dataComment = CommentSerializer(comment, many=True).data
				dataComment = []
				totalComment = 0
				for comment in comments:
					dComment = CommentSerializer(comment).data
					reply = Comment.objects.filter(to_post_id = post, to_comment_id = comment)
					if len(reply) > 0:
						dComment["reply"] = CommentSerializer(reply, many=True).data
						totalComment += len(reply)
					else:
						dComment['reply'] = []

					totalComment += 1
					dataComment.append(dComment)
				data = PostSerializer(post).data
				return Response({"data":{"post":data, "comment": {"total":totalComment, "data":dataComment}}})

		except AssertionError as error:
			return AssertionErrorResponse({"msg":error.__str__()}, 404)

class CommentView(APIView):
	def post(self, request, versions):
		try:
			assert versions in API_VERSION, "version not found"
			if versions == 'v1':
				data = request.data
				serializer = CommentSerializer(data = data)
				print(data)
				print(serializer)
				print(serializer.is_valid())
				if serializer.is_valid():
					saved = serializer.save()
					return Response({"data":CommentSerializer(saved).data})

				else:
					raise

		except AssertionError as error:
			return AssertionErrorResponse({"msg":error.__str__()}, 400)

		except:
			return BadRequestResponse({"msg":"Bad Request"})

