from django.urls import path

from newspaper import views
from newspaper.views import contact_view, contact_success

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.PostsListView.as_view(), name="posts-list"),
    path("posts/create/", views.PostsCreateView.as_view(), name="posts-create"),
    path(
        "posts/<int:pk>/update/", views.PostsUpdateView.as_view(), name="posts-update"
    ),
    path(
        "posts/<int:pk>/delete/", views.PostsDeleteView.as_view(), name="posts-delete"
    ),
    path("posts/<int:pk>/", views.PostsDetailView.as_view(), name="posts-detail"),
    path("topic/", views.TopicsListView.as_view(), name="topic-list"),
    path("topic/create/", views.TopicsCreateView.as_view(), name="topic-create"),
    path(
        "topic/<int:pk>/update/", views.TopicsUpdateView.as_view(), name="topic-update"
    ),
    path(
        "topic/<int:pk>/delete/", views.TopicsDeleteView.as_view(), name="topic-delete"
    ),
    path("topic/<int:pk>/", views.TopicsDetailView.as_view(), name="topic-detail"),
    path("contact/", contact_view, name="contact"),
    path("contact/success/", contact_success, name="contact_success"),
]

app_name = "newspaper"
