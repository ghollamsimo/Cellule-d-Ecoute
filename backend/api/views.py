from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken, Token

from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def Register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return JsonResponse({
            'message': 'User registered successfully',
        })
    else:
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Please provide both email and password'}, status=400)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            token = RefreshToken.for_user(user)
            return JsonResponse({'token': str(token.access_token)})
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)