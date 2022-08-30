from django.views.generic import ListView
from .models import User
# Create your views here.

class ListListView(ListView):
    model = User
    template_name = 'todo_app/index.html'