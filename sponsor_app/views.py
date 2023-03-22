from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Sponsorpost
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
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
# def my_posts(request):
#     business_name = request.user
#     posts = Sponsorpost.objects.filter(business_name=request.user)
#     return render(request, 'sponsor_page.html', {'my_posts': my_posts})
