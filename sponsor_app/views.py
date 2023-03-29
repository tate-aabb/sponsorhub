from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Sponsorpost
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import SponsorForm
from ideas.forms import Add_Ideas
from ideas.models import IdeasModel
from accounts.models import Type, CustomUser




class SponsorPost(ListView):
        model = IdeasModel
        template_name = "sponsor.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            custom_user = None
            if self.request.user.is_authenticated:
                custom_user = self.request.user.custom_user.get().user_type
            context['custom_user'] = custom_user
            context['custom_users'] = CustomUser.objects.all()  # add data from other model
            return context


class SponsorDetail(DetailView):
    model = Sponsorpost
    template_name = "detail_sponsor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

def NewSponsorPost(request):
    user = request.user
    if user.is_authenticated:
        custom_user = user.custom_user.get().user_type
    else:
        custom_user = None
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("sponsor")
    else:
        form = SponsorForm
    context = {
        "custom_user": custom_user,
        "form": form
    }
    return render(request, "sponsor_form.html", context)

class SponsorUpdate(UpdateView):
    form_class = SponsorForm
    model = Sponsorpost
    template_name = "Sponsor_update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

class SponsorDelete(DeleteView):
    model = Sponsorpost
    template_name = "Sponsor_delete.html"
    success_url = reverse_lazy("sponsor")
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
    template_name = "sponsor.html"
    context_object_name = "sponsor"
    def get_queryset(self):
        query = self.request.GET.get("searchIdeas")
        return IdeasModel.objects.filter(Title__icontains=query)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

class Suser_accaunt(ListView):
    model = Sponsorpost
    template_name = "Suser_accaunt.html"
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)
        else:
            queryset = Sponsorpost.objects.none()
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context

class Detail_Contributor(DetailView):
    model = IdeasModel
    template_name = "detail_Contributor.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = None
        if self.request.user.is_authenticated:
            custom_user = self.request.user.custom_user.get().user_type
        context['custom_user'] = custom_user
        context['custom_users'] = CustomUser.objects.all()  # add data from other model
        return context