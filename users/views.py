from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from users.models import User, Confirmation
from users.serializers import UserCreateSerializer

import random
from datetime import timedelta
from django.utils import timezone


@api_view(['POST'])
def confirmation_api_view(request):
    user_id = request.data.get('user_id')
    confirmation_code = request.data.get('confirmation_code')

    try:
        user = User.objects.get(id=user_id)
        confirmation = Confirmation.objects.get(user=user)

        if confirmation.code == confirmation_code and confirmation.expires_at > timezone.now():
            user.is_confirmed = True
            user.save()
            confirmation.delete()
            return Response(status=status.HTTP_200_OK,
                            data={'message': 'User confirmed successfully.'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'message': 'Invalid or expired confirmation code.'})

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'User not found.'})
    except Confirmation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Confirmation code not found.'})


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = User.objects.create(username=username,
                               email=email,
                               is_confirmed=False)

    user.set_password(password)
    user.save()

    confirmation_code = random.randint(100000, 999999)

    expires_at = timezone.now() + timedelta(hours=1)

    confirmation = Confirmation.objects.create(user=user,
                                               code=confirmation_code,
                                               expires_at=expires_at)

    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id, 'message': f'Here is your confirmation code - {confirmation.code}'})
