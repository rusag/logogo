from django.urls import path
from . import views



urlpatterns = [
	# path('brand', views.brand_view,name='brand'),
	path('home', views.home, name='home'),
	# path('industry', views.industry_list_view ,name='industry'),
	# path('style', views.style_view,name='style')

]
