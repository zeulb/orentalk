from django.conf.urls import include, url

urlpatterns = [
	url(r'^(\d+)/$', 'chat.views.room_page', name='room'),
]