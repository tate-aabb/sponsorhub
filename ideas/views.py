from django.views.generic import ListView, DetailView
from .models import IdeasModel
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from accounts.models import Type, CustomUser
from .forms import Add_Ideas
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import Type, CustomUser


# @user_passes_test(lambda user: user.custom_user.get().user_type == Type.CONTRIBUTOR)

# @login_required
class IdeasBlog(ListView):
    model = IdeasModel
    template_name = 'ideas.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context



# @user_passes_test(lambda user: user.custom_user.get().user_type == Type.CONTRIBUTOR)
# @login_required
class IdeasDetail(DetailView):
    model = IdeasModel
    template_name = 'ideas_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

# @login_required
class NewIdeas(CreateView):
    form_class = Add_Ideas
    model = IdeasModel
    template_name = 'New_ideas.html'
    # fields = ["Title", "About_contributor", "Idea_industry", "Idea_text", "Budget", "Contact_email"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context



class IdeasUpdate(UpdateView):
    form_class = Add_Ideas
    model = IdeasModel
    template_name = 'ideas_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

class IdeasDelete(DeleteView):
    model = IdeasModel
    template_name = 'ideas_delete.html'
    success_url = reverse_lazy('ideas')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context


class IdeaSearch(ListView):
    model = IdeasModel
    template_name = 'ideas.html'
    context_object_name = 'ideas'

    def get_queryset(self):
        query = self.request.GET.get('searchIdea')
        return IdeasModel.objects.filter(Title__icontains=query)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

