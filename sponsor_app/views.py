from django.views.generic import ListView
from .models import Post, Sponsorpost
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,  redirect
from .forms import SponsorForm
from django.urls import reverse

def sponsor_view(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('sponsor'))
    # else:
    #     form = SponsorForm()
    # return render(request, 'sponsor_form.html', {'form': form})
    else:
        form = SponsorForm()
        return render(request, 'sponsor_form.html', {'form': form})
"""
class SponsorCreateView(CreateView):

    model = Sponsorpost
    template_name = 'sponsor_form.html'
    fields = ['business_name', 'about_sponsor', 'business_industry', 'budget', 'email']
"""
class BlogListView(ListView):

    model = Post
    template_name = 'sponsor.html'

@login_required
def my_posts(request):
    business_name = request.user
    posts = Sponsorpost.objects.filter(business_name=request.user)
    return render(request, 'sponsor_page.html', {'my_posts': my_posts})
