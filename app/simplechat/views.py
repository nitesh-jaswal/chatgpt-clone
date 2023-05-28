from decimal import Decimal

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseNotAllowed

from .forms import QnAForm
from .models import Question, Answer

# Create your views here.

def _get_llm_response(question: Question) -> Answer:
    # TODO: OpenAI response
    return Answer.objects.create(
        question = question,
        answer_text = "This is a sample answer!",
        cost = Decimal(0.001),
        tokens = 100
    )

def get_answer(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        qna = QnAForm(request.POST)
        if qna.is_valid():
            question_text = qna.cleaned_data['question']
            question = Question.objects.create(question_text=question_text)
            question.save()

            answer = _get_llm_response(question)
            answer.save()
            return render(request, "index.html", context=dict(question=question_text, answer=answer))
        return render(request, "index.html", context=dict(question=request.POST.get("question", ""), answer=""))

    return HttpResponseNotAllowed(permitted_methods=['POST'])

def letschat(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", context=dict(answer=""))
