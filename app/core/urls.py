from django.urls import path

from core.views.coreViews import PostView, PostDetail, CommentView

urlpatterns = [
	path('', PostView.as_view()),
	path('comment/', CommentView.as_view()),
	path('<slug:post_id>/', PostDetail.as_view())
]