from django.urls import path
from .views import UserLoginView, HomeView, UserLogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
