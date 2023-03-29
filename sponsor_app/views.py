from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Sponsorpost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import SponsorForm
from ideas.forms import Add_Ideas
from ideas.models import IdeasModel
from accounts.models import Type, CustomUser



class New_post(CreateView):
    model = Sponsorpost
    form_class = SponsorForm
    template_name = "sponsor_form.html"

    def get_success_url(self):
        return reverse_lazy('sponsorapp:sponsor')


@login_required()
@user_passes_test(lambda user: user.custom_user.get().user_type == Type.SPONSOR)
def for_sponsors(request):
    Ideas = IdeasModel.objects.all()
    return render(request, "sponsor.html", {"Ideas": Ideas})


# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = SponsorForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             return redirect('sponsor_page')
#     else:
#         form = SponsorForm()
#     return render(request, 'sponsor_page.html', {'form': form})


@login_required
def user_posts(request):
    posts = Sponsorpost.objects.filter(user=request.user)
    return render(request, 'sponsor_page.html', {'posts': posts})

class SponsorDetail(DetailView):
    model = Sponsorpost
    template_name = 'sponsor_detail.html'

class SponsorUpdate(UpdateView):
    model = Sponsorpost
    template_name = 'sponsor_update.html'
    fields = ['user', 'business_name', 'business_industry', 'about_sponsor', 'budget', 'email']


class SponsorDelete(DeleteView):
    model = Sponsorpost
    template_name = 'sponsor_delete.html'
    success_url = reverse_lazy('ideas')


class SponsorSearch(ListView):
    model = Sponsorpost
    template_name = 'sponsor.html'
    context_object_name = 'sponsor'

    def get_queryset(self):
        query = self.request.GET.get('searchSponsor')
        return Sponsorpost.objects.filter(business_industry__icontains=query)

