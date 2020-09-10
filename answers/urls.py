
from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_answer, name="add_answer"),
    path("delete/<int:answer_pk>", views.delete_answer, name="delete_answer"),
    path("edit/<int:answer_pk>", views.edit_answer, name="edit_answer"),
    path("list/", views.list_answer, name="list_answer"),
    path("view/<int:answer_pk>", views.view_answer, name="view_answer"),
]