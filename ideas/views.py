from django.views.generic import TemplateView
from .models import IdeasModel
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .forms import Add_Ideas
from sponsor_app.models import Sponsorpost
from sponsor_app.forms import SponsorForm

def IdeasBlog(request):
    Sponsor = Sponsorpost.objects.all()
    return render(request, "ideas.html", {"Sponsor": Sponsor})



class IdeasPage(FormView):
    form_class = SponsorForm
    template_name = "ideas.html"

class New_Ideas(CreateView):
    form_class = Add_Ideas
    template_name = "New_ideas.html"