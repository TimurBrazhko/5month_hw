from django.urls import path
from users.views import (registration_api_view, confirmation_api_view)
from rest_framework.authtoken.views import (obtain_auth_token,)


app_name = 'users'

urlpatterns = [
    path('signup/', registration_api_view, name='create_user_api_view'),
    path('login/', obtain_auth_token, name='login_api_view'),
    path('confirm/', confirmation_api_view, name='confirm_api_view'),
]
