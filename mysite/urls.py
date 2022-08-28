from django.contrib import admin
from django.urls import path,include
from chatting_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatting_app.urls')),
]
