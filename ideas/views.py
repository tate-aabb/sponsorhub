from django.views.generic import TemplateView
from .models import IdeasModel
from django.views.generic.edit import CreateView
from .forms import Add_Ideas


class IdeasPage(TemplateView):
    template_name = "ideas.html"

class New_Ideas(CreateView):
    form_class = Add_Ideas
    template_name = "New_ideas.html"