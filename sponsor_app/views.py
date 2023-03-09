from django.views.generic import ListView
from .models import Post
from django.views.generic.edit import CreateView

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
