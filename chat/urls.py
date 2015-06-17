from django.conf.urls import include, url

urlpatterns = [
	url(r'^newroom$', 'chat.views.new_room', name='new_room'),
]