from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView

from app.utils import BadRequestResponse, AssertionErrorResponse

from core.models.postModels import Post, Comment, Tag
from core.models.userModels import Profile, Friend, Notification
from core.serializers.postSerializer import PostSerializer, CommentSerializer
from core.serializers.userSerializer import ProfileSerializer, FriendSerializer, NotificationSerializer
from core.tools.encryptions import set_password, verify_password

API_VERSION = settings.API_VERSION


class NotificationView(APIView):
	def get(self, request, versions, user_id):
		try:
			assert versions in API_VERSION, "version not found"
			if versions == 'v1':
				profile = Profile.objects.get(user_id = user_id)
				notification = Notification.objects.filter(to_id = profile)
				data = NotificationSerializer(notification, many=True).data
				return Response({"data":{"total":len(notification), "data":data}})

		except AssertionError as error:
			return AssertionErrorResponse({"msg":error.__str__()}, 404)

class NotificationDetail(APIView):
	def get(self, request, versions, user_id, id):
		try:
			assert versions in API_VERSION, "version not found"
			# accept friend invitation
			ACCEPT_URL = settings.THIS_HOST + '/api/user/{}/friend/'.format(versions)
			if versions == 'v1':
				profile = None
				try:
					profile = Profile.objects.get(user_id = user_id)
				except:
					return Response({"error": [{"msg":"user id not found"}]}, status = 404)
				
				notification = Notification.objects.get(id = id)
				if notification.is_seen == False:
					# set notification as seen
					notification.is_seen = True
					notification.save()

				if notification.type == "friend":
					dataFriend = Friend.objects.get(invitation_id = notification.uid)
					data = {
						"notification": NotificationSerializer(notification).data, 
						"data":FriendSerializer(dataFriend).data
					}
					if dataFriend.is_accepted == None:
						data["accept"] = ACCEPT_URL + notification.uid + "?confirm=true",
						data["decline"] = ACCEPT_URL + notification.uid + "?confirm=false",
				
				return Response({
					"data": data
				})

		except AssertionError as error:
			return AssertionErrorResponse({"msg":error.__str__()}, 404)
