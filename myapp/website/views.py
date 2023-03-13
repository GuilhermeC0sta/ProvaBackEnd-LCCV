from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Olá, estranho. Adicione um /admin no final da URL para acessar o painel de administração.")

def helloWorld(request):
    return HttpResponse('Hello World')

'''def taskLIst(request):
    return render(request, 'taskList.html')'''