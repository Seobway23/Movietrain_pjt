from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('<str:username>/', views.user_profile),
    path('findusername/', views.find_username),
]
