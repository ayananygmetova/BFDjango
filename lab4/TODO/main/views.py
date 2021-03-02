from django.shortcuts import render

from main.models import Task, Todo


def todo_tasks(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        tasks = Task.objects.filter(todo=todo, completed=False)
        # date - en_formats.DATE_FORMAT = "d/m/Y" - in settings.py
        context = {"todo": todo, "tasks": tasks, "completed": False}
        return render(request, 'todo_list.html', context=context)
    except Todo.DoesNotExist:
        return render(request, '404.html')


def completed_tasks(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        tasks = Task.objects.filter(todo=todo, completed=True)
        context = {"todo": todo, "tasks": tasks, "completed": True}
        return render(request, 'completed_todo_list.html', context=context)
    except Todo.DoesNotExist:
        return render(request, '404.html')
