from django.urls import path 
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/detail/", views.detail, name="detail"),
    path("browse/", views.browse, name="browse"),
    path("new/", views.new, name="new"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("<int:id>/delete/", views.delete, name="delete"),
    path("<int:id>/edit/", views.edit, name="edit"),
]
