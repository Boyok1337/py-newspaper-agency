from datetime import timezone

from django.test import TestCase
from django.contrib.auth import get_user_model
from newspaper.models import Topic, Newspaper, ContactForm


class RedactorTestCase(TestCase):
    def setUp(self):
        self.redactor = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
            years_of_experience=5
        )

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor), 'testuser (Test User)')

    def test_redactor_ordering(self):
        redactor2 = get_user_model().objects.create_user(
            username='testuser2',
            password='testpassword',
            first_name='Test',
            last_name='User2',
            years_of_experience=3
        )
        self.assertEqual(
            list(get_user_model().objects.all()),
            [self.redactor, redactor2]
        )


class TopicTestCase(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name='Test Topic')

    def test_topic_str(self):
        self.assertEqual(str(self.topic), 'Test Topic')

    def test_topic_ordering(self):
        topic2 = Topic.objects.create(name='Test Topic2')
        self.assertEqual(
            list(Topic.objects.all()),
            [self.topic, topic2]
        )


class NewspaperTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.redactor = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
            years_of_experience=5
        )
        cls.topic = Topic.objects.create(name='Test Topic')
        cls.newspaper = Newspaper.objects.create(
            title='Test Newspaper',
            content='Test content',
            image_url='https://example.com/image.jpg'
        )
        cls.newspaper.topics.add(cls.topic)
        cls.newspaper.publishers.add(cls.redactor)

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper), 'Test Newspaper')

    def test_newspaper_ordering(self):
        newspaper2 = Newspaper.objects.create(
            title='Test Newspaper2',
            content='Test content2',
            image_url='https://example.com/image2.jpg'
        )
        newspaper2.topics.add(self.topic)
        newspaper2.publishers.add(self.redactor)
        self.assertEqual(
            list(Newspaper.objects.all().order_by('-published_date')),
            [newspaper2, self.newspaper]
        )

    def test_get_publishers(self):
        self.assertEqual(self.newspaper.get_publishers(), 'testuser')


class ContactFormTestCase(TestCase):
    def setUp(self):
        self.contact_form = ContactForm.objects.create(
            name='Test Name',
            email='test@example.com',
            message='Test message'
        )

    def test_contact_form_str(self):
        expected_str = f"{self.contact_form.name} {self.contact_form.email}{self.contact_form.message}{self.contact_form.submitted_at}"
        self.assertEqual(str(self.contact_form), expected_str)
