from django.urls import path

from newspaper import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.PostsListView.as_view(), name="posts-list"),
    path("posts/create", views.PostsCreateView.as_view(), name="posts-create"),
    path("posts/<int:pk>/update", views.PostsUpdateView.as_view(), name="posts-update"),
    path("posts/<int:pk>/delete", views.PostsDeleteView.as_view(), name="posts-delete"),
    path("posts/<int:pk>", views.PostsDetailView.as_view(), name="posts-detail"),
    path("topics/", views.TopicsListView.as_view(), name="topics-list"),
    path("topics/create", views.TopicsCreateView.as_view(), name="topics-create"),
    path("topics/<int:pk>/update", views.TopicsUpdateView.as_view(), name="topics-update"),
    path("topics/<int:pk>/delete", views.TopicsDeleteView.as_view(), name="topics-delete"),
    path("topics/<int:pk>", views.TopicsDetailView.as_view(), name="topics-detail"),

]

app_name = "newspaper"
