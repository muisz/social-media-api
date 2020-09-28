from django.urls import path

from core.views.login import LoginUser, RegisterUser

urlpatterns = [
	path('', RegisterUser.as_view()),
	path('login/', LoginUser.as_view())
]