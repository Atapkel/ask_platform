from django.shortcuts import render, redirect, get_object_or_404

from .forms import QuestionForm
from .forms import CommentForm
from .models import Question, Comment


# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'questions/all_questions.html', context)


def detail(request, id):
    question = Question.objects.get(id=id)
    comments = Comment.objects.filter(question=question)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.save()
            return redirect('question_detail', id=id)
    else:
        form = CommentForm()
    return render(request, 'questions/view_question.html', {'question': question,
                                                     'form': form,
                                                     'comments': comments})



def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = QuestionForm()

    return render(request, 'questions/create_question.html', {'form': form})

def update(request, id):
    question = get_object_or_404(Question, id=id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = QuestionForm(instance=question)

    return render(request, 'questions/update_question.html', {'form': form, 'question': question})


def delete(request, id):
    question = get_object_or_404(Question, id=id)

    if request.method == "POST":
        question.delete()
        return redirect("index")

    return render(request, 'questions/delete_question.html', {'question': question})

