from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, get_user_questions
from .forms import QuestionForm

# Create your views here.
def ask_question(request):
    if request.method == "GET":
        form = QuestionForm()
    else:
        if form.is_valid():
            question = form.save(commit=False)
            question.question_of = request.list_user_questions
            question.save()
            return redirect("list_user_questions")
    return render(request, "questions/ask_question.html", {
        "form": form
    })


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method="POST":
        question.delete()
        return redirect("list_question")
    return render(request, "questions/delete_question", {
        "question": question
    })


def list_question(request):
    questions = Question.objects.all()
    return render(request, "questions/list_question.html", {
        "questions": questions
    })


def list_user_questions(request):
    questions = Question.objects.get_user_questions(self.request.user)
    return render(request, "questions/list_user_questions", {
        "questions": questions
    })


def search_question(request):
    pass


def search_question_results(request):
    pass


def view_question(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, "questions/view_question.html", {
        "question": question
    })