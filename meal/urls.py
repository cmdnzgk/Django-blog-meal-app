from django.urls import path
from . import views

urlpatterns = [
    path("", views.meal_list, name="meal_list"),
    path("meal/<int:id>/", views.meal_detail, name="meal_detail"),
    path("create/", views.meal_create, name="meal_create"),
    path("update/<int:id>/", views.meal_update, name="meal_update"),
    path("delete/<int:id>/", views.meal_delete, name="meal_delete"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
]