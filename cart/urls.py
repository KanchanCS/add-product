from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout, name="logout"),
    path("add_product", views.add_product, name="add_product"),
    path("details/<int:id>/", views.product_details, name="product_details"),
    path("edit/<int:id>/", views.edit_product, name="edit_product"),
    path("delete/<int:id>/", views.delete_product, name="delete_product"),
]
