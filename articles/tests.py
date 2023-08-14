from django.contrib.auth import get_user_model,authenticate
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import status

from .models import Article

User = get_user_model()


#  전체 확인
# python manage.py test
#  앱 단위로 확인
# python manage.py test [앱이름]


# 아티클 CRUD 테스트코드
class ArticleCreateTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser',password ="12345678")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.client.login(email='test@test')
        Article.objects.create(title='test1' ,content='content1' ,user = self.user,pk=1)
        Article.objects.create(title='test2' ,content='content2' ,user = self.user,pk=2)

    def test_create(self):
        url = reverse('create')
        user_data = {
            "title":"테스트글입니다",
            "content":'내용!',
        }
        response = self.client.post(url,user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail(self):
        url = reverse('detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list(self):
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        url = reverse('update', kwargs={'pk': 1} )
        data = {"title": "업데이트", "content": "업데이트성공"}
        response = self.client.put(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_delete(self):
        url = reverse('delete', kwargs={'pk': 1} )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
