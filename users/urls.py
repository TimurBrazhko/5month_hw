from django.urls import path
from users.views import (ConfirmationAPIView, RegistrationAPIView)
from rest_framework.authtoken.views import (obtain_auth_token,)


app_name = 'users'

urlpatterns = [
    path('signup/', RegistrationAPIView.as_view(), name='create_user_api_view'),
    path('login/', obtain_auth_token, name='login_api_view'),
    path('confirm/', ConfirmationAPIView.as_view(), name='confirm_api_view'),
]
