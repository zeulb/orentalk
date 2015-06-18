from django.conf.urls import include, url

urlpatterns = [
	url(r'^register$', 'account.views.register', name='register'),
]