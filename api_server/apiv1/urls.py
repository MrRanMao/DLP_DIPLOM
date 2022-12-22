from django.urls import path
from . import views

urlpatterns = [
	path('auth/check/', views.auth_check, name='api_v1_auth_check'),
	path('hash/add/', views.add_hash_view, name='api_v1_add_hash'),
	path('hash/del/', views.del_hash_view, name='api_v1_del_hash'),
	path('hash/check/<str:hash>', views.check_hash_view, name='api_v1_check_hash'),
]
