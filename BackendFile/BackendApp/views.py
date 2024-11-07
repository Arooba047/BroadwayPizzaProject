# views.py
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from rest_framework import generics, permissions
from .serializers import CartItemSerializer
# from django.http import JsonResponse, HttpResponseForbidden
# from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail

#Login and register views

class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')

        # Check if a user with this email or phone already exists
        if User.objects.filter(email=email).exists():
            return Response({'error': 'A user with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=phone).exists():
            return Response({'error': 'A user with this phone number already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create(
            username=phone,  
            email=email,
            password=make_password(password)  
        )
        subject = 'Registration Successfull'
        message = f'Hi {email}, You have sucessfully registered in broadway pizza website.'
        email_from = 'aroobaiqbal118@gmail.com'
        rec_list = [email,]
        send_mail(subject, message, email_from, rec_list)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id
        }, status=status.HTTP_201_CREATED)
        subject = 'Registration Successfull'



class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')

        # Authenticate using either email or phone and password
        user = authenticate(request, email=email, password=password, phone=phone)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


#Add to cart views

class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        product_name = request.data.get('product_name')
        quantity = request.data.get('quantity', 1)
        price = request.data.get('price')
        product_id = request.data.get('product_id')
        
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product_id=product_id,
            defaults={'product_name': product_name, 'quantity': quantity, 'price': price}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response(CartItemSerializer(cart_item).data)

class CartItemListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


