from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.UserCreate.as_view(), name='users_create'),
    path('users/', views.UserList.as_view(), name='users_list'),
    path('users/<uuid:pk>/', views.UserDetail.as_view(), name='user_detail')
]