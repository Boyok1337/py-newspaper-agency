from django.contrib.auth import login
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from newspaper.models import Redactor, Newspaper, Topic
from newspaper.forms import (
    RegistrationForm,
    TopicForm,
    TopicUpdateForm,
    NewspaperForm, ContactFormForm,
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
    model = Newspaper
    template_name = "newspaper/newspaper_list.html"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            return Newspaper.objects.none()
        return Newspaper.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(topics__name__icontains=query) |
            Q(publishers__username__icontains=query)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


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
    success_url = reverse_lazy("newspaper:posts-list")


class PostsUpdateView(generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("newspaper:posts-detail", kwargs={"pk": pk})


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
    success_url = reverse_lazy("newspaper:topic-list")

    def form_valid(self, form):
        responce = super().form_valid(form)
        self.object = form.save()
        newspapers = form.cleaned_data.get("newspapers")
        if newspapers:
            self.object.newspapers.add(*newspapers)
        return responce


class TopicsUpdateView(generic.UpdateView):
    model = Topic
    form_class = TopicUpdateForm

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('newspaper:topic-detail', kwargs={'pk': pk})


class TopicsDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")


class TopicsDetailView(generic.DetailView):
    model = Topic


def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newspaper:contact_success')
    else:
        form = ContactFormForm()
    return render(request, 'contact/contact_form.html', {'form': form})


def contact_success(request):
    return render(request, 'contact/contact_success.html')