from rest_framework.response import Response
from rest_framework.views import APIView

from app.utils import BadRequestResponse

from core.models.postModels import Post, Comment
from core.models.userModels import Profile
from core.serializers.postSerializer import PostSerializer, CommentSerializer
from core.serializers.userSerializer import ProfileSerializer
from core.tools.encryptions import set_password, verify_password

class LoginUser(APIView):
	def post(self, request):
		try:
			data = request.data
			email = data.get('email')
			password = data.get('password')
			c_pass = Profile.objects.get(email = email)
			passCheck = verify_password(password, c_pass.password)
			if passCheck:
				return Response({"data": {"msg":"login success"}})
			return Response({"data": {"msg":"email/password invalid"}})

		except:
			return BadRequestResponse({"msg": "Bad Request"})

class RegisterUser(APIView):
	def post(self, request):
		try:
			data = request.data
			password = data.get('password')
			data['password'] = set_password(password)
			serializer = ProfileSerializer(data = data)
			if serializer.is_valid():
				saved = serializer.save()
				return Response(ProfileSerializer(saved).data)

			else:
				raise

		except:
			return BadRequestResponse({"msg": "Bad Request"})

	def get(self, request):
		profile = Profile.objects.all()
		data = ProfileSerializer(profile, many=True).data
		return Response({"data": data})