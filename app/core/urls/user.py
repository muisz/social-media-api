from django.urls import path

from core.views.login import LoginUser, RegisterUser
from core.views.coreViews import FriendView, ConfirmFriendRequest
from core.views.notification import NotificationView, NotificationDetail

urlpatterns = [
	path('', RegisterUser.as_view()),
	path('login/', LoginUser.as_view()),
	path('<str:versions>/friends/', FriendView.as_view()),
	path('<str:versions>/friends/<slug:invitation_id>/', ConfirmFriendRequest.as_view()),

	path('<str:versions>/notification/<slug:user_id>/', NotificationView.as_view()),
	path('<str:versions>/notification/<slug:user_id>/<int:id>/', NotificationDetail.as_view())
]