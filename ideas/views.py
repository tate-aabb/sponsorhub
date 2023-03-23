from django.views.generic import ListView, DetailView
from .models import IdeasModel
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import Add_Ideas
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import Type, CustomUser


# @user_passes_test(lambda user: user.custom_user.get().user_type == Type.CONTRIBUTOR)

# @login_required
class IdeasBlog(ListView):
    model = IdeasModel
    template_name = 'ideas.html'


# @user_passes_test(lambda user: user.custom_user.get().user_type == Type.CONTRIBUTOR)
# @login_required
class IdeasDetail(DetailView):
    model = IdeasModel
    template_name = 'ideas_detail.html'


# @login_required
class NewIdeas(CreateView):
    model = IdeasModel
    template_name = 'New_ideas.html'
    fields = ["Title", "About_contributor", "Idea_industry", "Idea_text", "Budget", "Contact_email"]


class IdeasUpdate(UpdateView):
    model = IdeasModel
    template_name = 'ideas_update.html'
    fields = ["Title", "About_contributor", "Idea_industry", "Idea_text", "Budget", "Contact_email"]


class IdeasDelete(DeleteView):
    model = IdeasModel
    template_name = 'ideas_delete.html'
    success_url = reverse_lazy('ideas')


def search(request):
    searchTerm = request.GET.get('searchIdea')
    if searchTerm:
        ideas = IdeasModel.objects.filter(title__icontains=searchTerm)
    else:
        ideas = IdeasModel.objects.all()
    return render(request, 'ideas.html',
                  {'searchTerm': searchTerm, 'ideas': ideas})


# def IdeasBlog(request):
#     Sponsor = Sponsorpost.objects.all()
#     return render(request, "ideas.html", {"Sponsor": Sponsor})



# class IdeasPage(FormView):
#     form_class = SponsorForm
#     template_name = "ideas.html"


#
