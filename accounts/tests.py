from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import status
from .serializers import bcypt_password
User = get_user_model()


#  전체 확인
# python manage.py test
#  앱 단위로 확인
# python manage.py test [앱이름]


#회원가입 
class UserSignupTest(APITestCase):
    def test_signup(self): #기본 회원가입
        url = reverse("signup")
        user_data = {
            "email":"test@test",
            "password":'password'
        }
        response = self.client.post(url,user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_signup(self): # 아이디 @ 체크 
        url = reverse("signup")
        user_data = {
            "email":"testtest",
            "password":'password'
        }
        response = self.client.post(url,user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#로그인
class UserLoginTest(APITestCase):
        def setUp(self): # 유저 생성
            password= password=bcypt_password('password')
            hash_password = password.decode()
            User.objects.create(email='test@test',password=hash_password)

        def test_login(self): # 회원가입 테스트 
            url = reverse("login")
            user_data = {
                "email":"test@test",
                "password":'password'
            }
            response = self.client.post(url,user_data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
        def test_count(self):#비밀번호 7자 이내 
            url = reverse("login")
            user_data = {
                "email":"test@test",
                "password":'passwod'
            }
            response = self.client.post(url,user_data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


