from django.conf.urls import include, url

urlpatterns = [
	url(r'^register$', 'account.views.register_page', name='register'),
	url(r'^login$', 'account.views.login_page', name='login'),
	url(r'^logout$', 'account.views.logout_page', name='logout'),
]