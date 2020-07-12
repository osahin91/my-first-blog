from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	#looks for /post/<passes post primary key to views as variable pk>/
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]