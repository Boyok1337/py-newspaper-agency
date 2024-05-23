from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from newspaper.models import Newspaper, Topic, ContactForm, Redactor
from newspaper.forms import (
    NewspaperForm,
    TopicForm,
    TopicUpdateForm,
)


class PostSearchViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.newspaper1 = Newspaper.objects.create(
            title="Test Post 1",
            content="Test content 1",
            image_url="http://example.com/image1.jpg",
        )
        self.newspaper2 = Newspaper.objects.create(
            title="Test Post 2",
            content="Test content 2",
            image_url="http://example.com/image2.jpg",
        )
        self.url = reverse("posts-search")

    def tearDown(self):
        self.newspaper1.delete()
        self.newspaper2.delete()

    def test_post_search_view_get_no_query(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")
        self.assertEqual(len(response.context_data["object_list"]), 0)

    def test_post_search_view_get_query(self):
        response = self.client.get(self.url + "?q=test")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")
        self.assertEqual(len(response.context_data["object_list"]), 2)
        self.assertIn(self.newspaper1, response.context_data["object_list"])
        self.assertIn(self.newspaper2, response.context_data["object_list"])


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("newspaper:index")

    def test_index_view_get(self):
        response = self.client.get(reverse("newspaper:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/index.html")
        template_context = response.context
        self.assertEqual(template_context["num_posts"], Newspaper.objects.count())
        self.assertEqual(template_context["num_topics"], Topic.objects.count())
        self.assertEqual(template_context["num_redactors"], Redactor.objects.count())


class PostsListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("newspaper:posts-list")
        self.newspaper1 = Newspaper.objects.create(
            title="Test Newspaper 1", content="Test content 1"
        )
        self.newspaper2 = Newspaper.objects.create(
            title="Test Newspaper 2", content="Test content 2"
        )

    def test_posts_list_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_list.html")
        self.assertEqual(len(response.context_data["object_list"]), 2)
        self.assertIn(self.newspaper1, response.context_data["object_list"])
        self.assertIn(self.newspaper2, response.context_data["object_list"])


class PostsCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Redactor.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.topic = Topic.objects.create(name="Test Topic")
        self.url = reverse("newspaper:posts-create")
        self.client.login(username="testuser", password="testpassword")

    def test_posts_create_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_form.html")
        self.assertIsInstance(response.context_data["form"], NewspaperForm)


class PostsUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper", content="Test content"
        )
        self.url = reverse("newspaper:posts-update", args=[self.newspaper.id])
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_posts_update_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_form.html")
        self.assertIsInstance(response.context_data["form"], NewspaperForm)

    def test_posts_update_view_post(self):
        def test_posts_update_view_post(self):
            data = {
                "title": "Updated Newspaper",
                "content": "Updated content",
                "image_url": "https://example.com/updated_image.jpg",
                "topics": self.topic.pk,
                "publishers": self.redactor.pk,
            }
            response = self.client.post(self.update_url, data=data)

            self.newspaper.refresh_from_db()

            self.assertEqual(self.newspaper.title, "Updated Newspaper")
            self.assertEqual(self.newspaper.content, "Updated content")
            self.assertEqual(
                self.newspaper.image_url, "https://example.com/updated_image.jpg"
            )
            self.assertEqual(self.newspaper.topics.first(), self.topic)
            self.assertEqual(self.newspaper.publishers.first(), self.redactor)

            self.assertRedirects(response, self.detail_url)


class PostsDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper", content="Test content"
        )
        self.url = reverse("newspaper:posts-delete", args=[self.newspaper.id])
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_posts_delete_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_confirm_delete.html")
        self.assertEqual(response.context_data["object"], self.newspaper)

    def test_posts_delete_view_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Newspaper.objects.filter(title="Test Newspaper").exists())


class PostsDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper", content="Test content"
        )
        self.url = reverse("newspaper:posts-detail", args=[self.newspaper.id])

    def test_posts_detail_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/newspaper_detail.html")
        self.assertEqual(response.context_data["object"], self.newspaper)


class TopicsListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("newspaper:topic-list")
        self.topic1 = Topic.objects.create(name="Test Topic 1")
        self.topic2 = Topic.objects.create(name="Test Topic 2")

    def test_topics_list_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/topic_list.html")
        self.assertEqual(len(response.context_data["object_list"]), 2)
        self.assertIn(self.topic1, response.context_data["object_list"])
        self.assertIn(self.topic2, response.context_data["object_list"])


class TopicsCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("newspaper:topic-create")
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_topics_create_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/topic_form.html")
        self.assertIsInstance(response.context_data["form"], TopicForm)

    def test_topics_create_view_post(self):
        data = {
            "name": "Test Topic",
            "newspapers": [1, 2],
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(name="Test Topic").exists())


class TopicsUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.topic = Topic.objects.create(name="Test Topic")
        self.url = reverse("newspaper:topic-update", args=[self.topic.id])
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_topics_update_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/topic_form.html")
        self.assertIsInstance(response.context_data["form"], TopicUpdateForm)

    def test_topics_update_view_post(self):
        data = {
            "name": "Updated Topic",
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
        self.topic.refresh_from_db()
        self.assertEqual(self.topic.name, "Updated Topic")


class TopicsDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.topic = Topic.objects.create(name="Test Topic")
        self.url = reverse("newspaper:topic-delete", args=[self.topic.id])
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_topics_delete_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/topic_confirm_delete.html")
        self.assertEqual(response.context_data["object"], self.topic)

    def test_topics_delete_view_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Topic.objects.filter(name="Test Topic").exists())


class TopicsDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.topic = Topic.objects.create(name="Test Topic")
        self.url = reverse("newspaper:topic-detail", args=[self.topic.id])

    def test_topics_detail_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newspaper/topic_detail.html")
        self.assertEqual(response.context_data["object"], self.topic)


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("newspaper:contact")

    def test_contact_view_get(self):
        response = self.client.get(reverse("newspaper:contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<input type="text" name="name"')
        self.assertContains(response, '<input type="email" name="email"')
        self.assertContains(response, '<textarea name="message"')

    def test_contact_view_post_valid_data(self):
        data = {
            "name": "Test Name",
            "email": "test@example.com",
            "message": "Test message",
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ContactForm.objects.filter(name="Test Name").exists())

    def test_contact_view_post_invalid_data(self):
        data = {
            "name": "",
            "email": "test@example.com",
            "message": "Test message",
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactForm.objects.filter(name="").exists())
        self.assertFormError(response, "form", "name", "This field is required.")
