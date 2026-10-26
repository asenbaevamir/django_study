from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('users/<str:username>/', views.user_detail, name='user_detail'),
    path('forum/', views.forum, name='forum'),
    path('contacts/', views.contacts, name='contacts'),
]
