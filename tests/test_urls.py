from django.urls import reverse
from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):
    def test_admin_url(self):
        url = reverse("admin:index")
        self.assertEqual(url, "/admin/")

    def test_register_url(self):
        url = reverse("register")
        self.assertEqual(url, "/register/")

    def test_login_url(self):
        url = reverse("login")
        self.assertEqual(url, "/accounts/login/")

    def test_logout_url(self):
        url = reverse("logout")
        self.assertEqual(url, "/accounts/logout/")

    def test_search_url(self):
        url = reverse("posts-search")
        self.assertEqual(url, "/search/")

    def test_index_url(self):
        url = reverse("newspaper:index")
        self.assertEqual(url, "/")

    def test_posts_list_url(self):
        url = reverse("newspaper:posts-list")
        self.assertEqual(url, "/posts/")

    def test_posts_create_url(self):
        url = reverse("newspaper:posts-create")
        self.assertEqual(url, "/posts/create/")

    def test_posts_update_url(self):
        url = reverse("newspaper:posts-update", args=[1])
        self.assertEqual(url, "/posts/1/update/")

    def test_posts_delete_url(self):
        url = reverse("newspaper:posts-delete", args=[1])
        self.assertEqual(url, "/posts/1/delete/")

    def test_posts_detail_url(self):
        url = reverse("newspaper:posts-detail", args=[1])
        self.assertEqual(url, "/posts/1/")

    def test_topic_list_url(self):
        url = reverse("newspaper:topic-list")
        self.assertEqual(url, "/topic/")

    def test_topic_create_url(self):
        url = reverse("newspaper:topic-create")
        self.assertEqual(url, "/topic/create/")

    def test_topic_update_url(self):
        url = reverse("newspaper:topic-update", args=[1])
        self.assertEqual(url, "/topic/1/update/")

    def test_topic_delete_url(self):
        url = reverse("newspaper:topic-delete", args=[1])
        self.assertEqual(url, "/topic/1/delete/")

    def test_topic_detail_url(self):
        url = reverse("newspaper:topic-detail", args=[1])
        self.assertEqual(url, "/topic/1/")

    def test_contact_url(self):
        url = reverse("newspaper:contact")
        self.assertEqual(url, "/contact/")

    def test_contact_success_url(self):
        url = reverse("newspaper:contact_success")
        self.assertEqual(url, "/contact/success/")
