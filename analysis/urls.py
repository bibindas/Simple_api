from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
				url(r'^topfive/$',views.TopFive.as_view(),name='topfive'),
				url(r'^companyshare/$',views.CompanyShare.as_view(),name='companyshare')
				
			]