from django.shortcuts import render, redirect, get_object_or_404
from .models import Answer
from questions.models import Question
from .forms import AnswerForm

# Create your views here.
def add_answer(request, question_pk):
    if request.method == "GET":
        form = AnswerForm()
    else:
        form = AnswerForm(request.POST)
        question = get_object_or_404(Question, pk=question_pk)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.answer_of = request.user
            answer.answer_to = question
            answer.save()
            return redirect("view_question", pk=pk)
    return render(request, "answers/add_answer.html", {
        "form": form,
        "answer": answer,
        "question": question
    })

def delete_answer(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.method == "POST":
        answer.delete()
        return redirect("list_answer")
    return render(request, "answers/delete_answer.html", {
        "answer": answer
    })


def edit_answer(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.method == "GET":
        form = AnswerForm(answer)
    else:
        form = AnswerForm(request.POST, answer)
        if form.is_valid:
            form.save()
            return redirect('list_answer')
    return render(request, "answers/edit_answer.html", {
        "form": form,
        "answer": answer
    })



def list_answer(request):
    answers = request.question.answers.all()
    return render(request, "answers/list_answer.html", {
        "answers": answers
    })


def view_answer(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    return render(request, "answers/view_answer.html", {
        "answer": answer
    })