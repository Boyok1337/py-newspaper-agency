from django.test import TestCase
from newspaper.forms import NewspaperForm, TopicForm, TopicUpdateForm, ContactFormForm
from newspaper.models import Redactor, Topic


class TestNewspaperForm(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="testredactor",
            email="testredactor@example.com",
            password="testpass",
        )

    def test_form_invalid_data(self):
        form_data = {
            "title": "",
            "description": "",
            "publishers": [],
        }
        form = NewspaperForm(data=form_data)
        self.assertFalse(form.is_valid())


class TestTopicForm(TestCase):
    def test_form_valid_data(self):
        form_data = {
            "name": "Test Topic",
        }
        form = TopicForm(data=form_data)
        self.assertTrue(form.is_valid())

        topic = form.save()
        self.assertEqual(topic.name, form_data["name"])

    def test_form_invalid_data(self):
        form_data = {
            "name": "",
        }
        form = TopicForm(data=form_data)
        self.assertFalse(form.is_valid())


class TestTopicUpdateForm(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Test Topic")

    def test_form_valid_data(self):
        form_data = {
            "name": "Updated Test Topic",
        }
        form = TopicUpdateForm(data=form_data, instance=self.topic)
        self.assertTrue(form.is_valid())

        topic = form.save()
        self.assertEqual(topic.name, form_data["name"])

    def test_form_invalid_data(self):
        form_data = {
            "name": "",
        }
        form = TopicUpdateForm(data=form_data, instance=self.topic)
        self.assertFalse(form.is_valid())


class TestContactFormForm(TestCase):
    def test_form_valid_data(self):
        form_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "message": "Test message",
        }
        form = ContactFormForm(data=form_data)
        self.assertTrue(form.is_valid())

        contact_form = form.save()
        self.assertEqual(contact_form.name, form_data["name"])
        self.assertEqual(contact_form.email, form_data["email"])
        self.assertEqual(contact_form.message, form_data["message"])

    def test_form_invalid_data(self):
        form_data = {
            "name": "",
            "email": "",
            "message": "",
        }
        form = ContactFormForm(data=form_data)
        self.assertFalse(form.is_valid())
