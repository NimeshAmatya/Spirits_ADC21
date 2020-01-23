from django.urls import path
#from .views import PostListView, PostDetailView
from . import views

urlpatterns=[
	#path('',PostListView.as_view(), name='roomfinder-home'),
	#path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
	#path('login/', views.about, name='roomfinder-login'),
	path('addpost/', views.add, name='addpost'),
]

