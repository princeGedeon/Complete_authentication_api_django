from django.urls import path

from accounts.views import UserProfileView,UserChangePasswordView,UserRegistrationView,UserLoginView

urlpatterns = [
   path('register/',UserRegistrationView.as_view(),name='register'),
   path('login/',UserLoginView.as_view(),name="login"),
   path('profile/',UserProfileView.as_view(),name="profile"),
path('changepassword/',UserChangePasswordView.as_view(),name="changepassword"),
]