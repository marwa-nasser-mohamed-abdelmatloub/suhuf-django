from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        open_actions = ['login', 'register', 'check_email', 'check_username', 'check_phone']
        if self.action in open_actions:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data,
                'message': 'تم تسجيل الحساب بنجاح'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': UserSerializer(user).data,
                    'message': 'تم تسجيل الدخول بنجاح'
                })
            else:
                return Response({
                    'message': 'اسم المستخدم أو كلمة المرور غير صحيحة'
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'تم تسجيل الخروج بنجاح'})
        except:
            return Response({'message': 'تم تسجيل الخروج بنجاح'})


    @action(detail=False, methods=['get'], url_path='check-email', permission_classes=[permissions.AllowAny])
    def check_email(self, request):
        email = request.query_params.get('email', None)
        user_id = request.query_params.get('id', None)
        if not email:
            return Response({'available': False, 'error': 'يرجى إدخال البريد الإلكتروني'}, status=status.HTTP_400_BAD_REQUEST)
        qs = CustomUser.objects.filter(email=email)
        if user_id:
            qs = qs.exclude(id=user_id)
        exists = qs.exists()
        return Response({'available': not exists})


    @action(detail=False, methods=['get'], url_path='check-username', permission_classes=[permissions.AllowAny])
    def check_username(self, request):
        username = request.query_params.get('username', None)
        user_id = request.query_params.get('id', None)
        if not username:
            return Response({'available': False, 'error': 'يرجى إدخال اسم المستخدم'}, status=status.HTTP_400_BAD_REQUEST)
        qs = CustomUser.objects.filter(username=username)
        if user_id:
            qs = qs.exclude(id=user_id)
        exists = qs.exists()
        return Response({'available': not exists})


    @action(detail=False, methods=['get'], url_path='check-phone', permission_classes=[permissions.AllowAny])
    def check_phone(self, request):
        phone = request.query_params.get('phone', None)
        user_id = request.query_params.get('id', None)
        if not phone:
            return Response({'available': False, 'error': 'يرجى إدخال رقم الهاتف'}, status=status.HTTP_400_BAD_REQUEST)
        qs = CustomUser.objects.filter(phone_number=phone)
        if user_id:
            qs = qs.exclude(id=user_id)
        exists = qs.exists()
        return Response({'available': not exists})