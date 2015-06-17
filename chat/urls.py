from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 'chat.views.room', name='room'),
]