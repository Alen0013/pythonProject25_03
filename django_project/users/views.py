from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Добро пожаловать в мой Django проект!")