from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Project

def project_list(request):
    """
    Получает все проекты со статусом 'completed' 
    и передает их в шаблон.
    """
    projects = Project.objects.filter(status='completed').order_by('-completion_date')
    return render(request, 'project/list.html', {'projects': projects})


class CustomLoginView(LoginView):
    """
    Стандартное представление Django для авторизации пользователей.
    Оно использует шаблон 'registration/login.html' по умолчанию.
    """
    template_name = 'registration/login.html'

# Создаем алиас-функцию, если в urls.py импортируется именно функция, а не класс
custom_login_view = CustomLoginView.as_view()
