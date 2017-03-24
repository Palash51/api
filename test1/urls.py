from django.conf.urls import url
from django.conf.urls import include
from test1 import views
from django.conf import settings
from django.conf.urls import  include, url
from django.conf.urls.static import static

# from rest_framework.urlpatterns import formate_suffix_patterns

urlpatterns = [
	url(r'^$', views.home, name = "homepage"),
	url(r'^api/$', views.Detail.as_view()),
	url(r'^api/getTransaction/$', views.Transaction.as_view()),
	url(r'^api/getParking/$', views.Parking.as_view()),
	url(r'^api/getUser/$', views.GetUser.as_view()),
	url(r'^api/getUserHistory', views.GetUserHistory.as_view()),
	# url(r'^api/(?P<pk>[0-9]+)/$', views.main.as_view()),
	
]

# urlpatterns = formate_suffix_patterns(urlpatterns)
