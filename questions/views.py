# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Min
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.postgres.search import SearchVector


# Project file imports
from .models import Question
from .forms import QuestionForm
from answers.models import Answer
from answers.forms import AnswerForm

# Create your views here.
@login_required(login_url="login_user")
def ask_question(request):
    if request.method == "GET":
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.question_of = request.user
            question.save()
            return redirect("list_user_questions")
    return render(request, "questions/ask_question.html", {
        "form": form
    })


@login_required(login_url="login_user")
def delete_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == "POST":
        question.delete()
        return redirect("list_question")
    return render(request, "questions/delete_question.html", {
        "question": question
    })


def list_question(request):
    questions = Question.objects.all()
    return render(request, "questions/list_question.html", {
        "questions": questions
    })


@login_required(login_url="login_user")
def list_user_questions(request):
    #questions = Question.objects.get_user_questions(self.request.user)
    questions = request.user.questions.all()
    return render(request, "questions/list_user_questions.html", {
        "questions": questions
    })


def search_question(request):
    query = request.GET.get("q")
    if query is not None:
        questions = Question.objects.annotate(
            search=SearchVector("question_title", "question_body")
        ).filter(search=query)
    else:
        questions = None
    return render(request, "questions/search_question.html", {
        "questions": questions,
        "query": query or ""
    })


def search_question_results(request):
    pass


@login_required(login_url="login_user")
def view_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    question = Question.objects.annotate(num_favorites=Count("favorited_by")).get(pk=question_pk)
    answers = question.answers.all()
    is_favorite_question = False
    if question in request.user.favorite_questions.all():
        is_favorite_question = True
    return render(request, "questions/view_question.html", {
        "question": question,
        "answers": answers,
        "AnswerForm": AnswerForm,
        "question_pk": question_pk,
        "is_favorite_question": is_favorite_question,
    })


@login_required(login_url="login_user")
@csrf_exempt
@require_POST
def toggle_fav_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if question in request.user.favorite_questions.all():
        request.user.favorite_questions.remove(question)
        return JsonResponse({"favorite_question": False})
    else:
        request.user.favorite_questions.add(question)
        return JsonResponse({"favorite_question": True})
