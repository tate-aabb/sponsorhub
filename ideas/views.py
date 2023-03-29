from django.views.generic import ListView, DetailView, TemplateView
from .models import IdeasModel
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import Add_Ideas
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import Type, CustomUser
from sponsor_app.models import Sponsorpost


# @user_passes_test(lambda user: user.custom_user.get().user_type == Type.CONTRIBUTOR)

# @login_required
class IdeasBlog(ListView):
    model = Sponsorpost
    template_name = 'ideas.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context




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
def NewIdeas(request):
    user = request.user
    if user.is_authenticated:
        custom_user = user.custom_user.get().user_type
    else:
        custom_user = None
    if request.method == "POST":
        form = Add_Ideas(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("user_account", username=request.user.username)
    else:
        form = Add_Ideas
    context = {
        "custom_user": custom_user,
        "form": form
    }
    return render(request, "New_ideas.html", context)
# class NewIdeas(CreateView):
#     form_class = Add_Ideas
#     model = IdeasModel
#     template_name = 'New_ideas.html'
#     # fields = ["Title", "About_contributor", "Idea_industry", "Idea_text", "Budget", "Contact_email"]
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         custom_user = None
#         if self.request.user.is_authenticated:
#             custom_user = self.request.user.custom_user.get().user_type
#         context['custom_user'] = custom_user
#         context['custom_users'] = CustomUser.objects.all()  # add data from other model
#         return context



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
    model = Sponsorpost
    template_name = 'ideas.html'
    context_object_name = 'ideas'

    def get_queryset(self):
        query = self.request.GET.get("searchSponsor")
        return Sponsorpost.objects.filter(business_name__icontains=query)
        # query = self.request.GET.get('searchIdea')
        # return IdeasModel.objects.filter(Title__icontains=query)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context


class User_account(ListView):
    model = IdeasModel
    template_name = 'user_account.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)
        else:
            queryset = IdeasModel.objects.none()
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

class Detail_Sponsors(DetailView):
    model = Sponsorpost
    template_name = 'details_sponsors.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

