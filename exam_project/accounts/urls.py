from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile')
]