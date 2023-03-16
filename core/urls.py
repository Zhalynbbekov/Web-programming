from django.urls import path
from core.views import SignUpView, ProfileView

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]