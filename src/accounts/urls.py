from django.urls import path

from accounts.views import UserRegistrationView

urlpatterns = [
   path('register/',UserRegistrationView.as_view(),name='register')
]