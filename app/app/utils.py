from rest_framework.response import Response

def generatePassword(password):
	s_pass = "f568bd30b435165954801cf90e94328{}dbf07628bb0086fd53b1d4eb7641fa500".format(password)
	return s_pass

def BadRequestResponse(error):
	return Response({"error": [error]}, status = 400)

def AssertionErrorResponse(error, code):
	return Response({"error": [error]}, status = code)
