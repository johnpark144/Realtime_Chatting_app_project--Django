from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'chatting_app' 

urlpatterns = [
    path('', views.chatting_room, name='chatting_room'),
    path('send/', views.send, name='send'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/<int:message_id>/', views.message_delete, name='message_delete'),
]
