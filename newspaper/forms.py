from django import forms

from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Redactor, Topic, Newspaper, ContactForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Redactor
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Choose a publishers",
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Choose a topic",
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]


class TopicUpdateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            "name",
        ]


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "message"]
