# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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


@login_required
def list_user_questions(request):
    #questions = Question.objects.get_user_questions(self.request.user)
    questions = request.user.questions.all()
    return render(request, "questions/list_user_questions.html", {
        "questions": questions
    })


def search_question(request):
    pass


def search_question_results(request):
    pass


def view_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    answers = question.answers.all()
    return render(request, "questions/view_question.html", {
        "question": question,
        "answers": answers,
        "AnswerForm": AnswerForm,
        "question_pk": question_pk
    })


def toggle_fav_question(request, question_pk):
    pass