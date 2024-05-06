from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from newspaper.models import Redactor, Newspaper, Topic
from newspaper.forms import (
    RegistrationForm,
    TopicForm,
    TopicUpdateForm,
    NewspaperForm
)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm
        return render(request,
                      "registration/register.html",
                      {"form": form})


class PostSearchView(generic.ListView):
    pass


def index(request):
    num_posts = Newspaper.objects.count()
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    context = {
        "num_posts": num_posts,
        "num_redactors": num_redactors,
        "num_topics": num_topics
    }

    return render(
        request, "newspaper/index.html", context=context
    )


class PostsListView(generic.ListView):
    model = Newspaper
    paginate_by = 8


class PostsCreateView(generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm


class PostsUpdateView(generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm


class PostsDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:posts-list")


class PostsDetailView(generic.DetailView):
    model = Newspaper


class TopicsListView(generic.ListView):
    model = Topic
    paginate_by = 8


class TopicsCreateView(generic.CreateView):
    model = Topic
    form_class = TopicForm

    def form_valid(self, form):
        responce = super().form_valid(form)
        self.object = form.save()
        newspapers = form.cleaned_data["newspapers"]
        if newspapers:
            self.object.newspapers.add(*newspapers)
        return responce


class TopicsUpdateView(generic.UpdateView):
    model = Topic
    form_class = TopicUpdateForm


class TopicsDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topics-list")


class TopicsDetailView(generic.DetailView):
    model = Topic
