from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("create/", views.post_create, name="post_create"),
    path("update/<int:id>/", views.post_update, name="post_update"),
    path("delete/<int:id>/", views.post_delete, name="post_delete"),
]