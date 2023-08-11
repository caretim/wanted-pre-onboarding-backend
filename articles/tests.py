from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import status

User = get_user_model()


#  전체 확인
# python manage.py test
#  앱 단위로 확인
# python manage.py test [앱이름]

def make_user():
    client = APIClient()
    User.objects.create(email="test@test", password="password")
    user = User.objects.get(email="test@test")
    client.force_authenticate(user=user)


class ArticleCreateTest(APITestCase):
    def test_create(self):
        make_user()
        url = reverse('article-post')
        user_data = {
            "title":"테스트글입니다",
            "content":'내용!'
        }
        response = self.client.post(url,user_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_detail(self):
        url = reverse('article-list')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, 200)


        # url = reverse('article-list', kwargs={'pk': 1})