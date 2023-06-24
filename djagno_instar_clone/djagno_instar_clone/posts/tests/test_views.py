from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile


class TestPost(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'ghostdog',
            email = 'lldp0506@naver.com',
            password = '12345678'
        )

    def test_get_posts_page(self):
        url = reverse('posts:post_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'posts/post_create.html')

        #makemigrations으로 post테이블 생성해야함. 이후 migrate까지 해주면됨

    def test_create_posts(self):
        login = self.client.login(username = "ghostdog",pawssword = "12345678")
        self.assertTrue(login)

        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg",b"whatevercontents")
        response = self.client.post(
            url,
            {"image":image,"caption":"test test"}
        )

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'posts/base.html')

    def test_create_posts_not_login(self):
        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg",b"whatevercontents")
        response = self.client.post(
            url,
            {"image":image,"caption":"test test"}
        )

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/main.html')

    