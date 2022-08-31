from django.views.generic import ListView
from .models import User, Task
# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'todo_app/index.html'

class TaskListView(ListView):
    model = Task
    template_name = 'todo_app/todo_task.html'

    def get_queryset(self):
        return Task.objects.filter(user_id=self.kwargs['task_id'])

    def get_context_data(self):
        context = super().get_context_data()
        context['user'] = User.objects.get(id=self.kwargs['task_id'])
        return context