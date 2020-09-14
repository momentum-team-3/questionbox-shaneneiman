
from django.urls import path
from . import views

urlpatterns = [
    path("ask/", views.ask_question, name="ask_question"),
    path("delete/<int:question_pk>", views.delete_question, name="delete_question"),
    path("list/", views.list_question, name="list_question"),
    path("list-user-questions/", views.list_user_questions, name="list_user_questions"),
    path("search/", views.search_question, name="search_question"),
    path("view/<int:question_pk>", views.view_question, name="view_question"),
    path("<int:question_pk>/favorite_question/", views.toggle_fav_question, name="toggel_fav_question"),
]