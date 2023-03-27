from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import ForbesList
from .forms import ContactForm
from accounts.models import CustomUser, User


def homepage(request):
    user = request.user
    if user.is_authenticated:
        custom_user = user.custom_user.get().user_type
    else:
        custom_user = None
    forbes_lists = ForbesList.objects.all()
    context = {'forbes_lists': forbes_lists,
               "custom_user": custom_user}
    return render(request, 'homepage.html', context)


def scrapeandsave(request):
    url = "https://www.forbes.com/forbes-400/"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')

    #Scraping the data
    for person in soup.find_all('div', {'class': 'Table_tableRow__M82uU'})[:16]:

        rank = person.find('div', {'class': 'Table_rank__KnjUY'}).text.replace('.', '')
        name = person.find('div', {'class': 'Table_personName__UO41W'}).text
        net_worth = person.find('div', {'class': 'Table_netWorth__py4xM'}).text
        age = person.find('div', {'class': 'Table_age__CHhfQ'}).text

        #Get scraped data, or create(srape)
        ForbesList.objects.get_or_create(rank=rank, name=name, net_worth=net_worth, age=age)

    return HttpResponse('Data successfully scraped')


def contact(request):
    user = request.user
    if user.is_authenticated:
        custom_user = user.custom_user.get().user_type
    else:
        custom_user = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ContactForm(request.POST)
    context = {"form": form,
               "custom_user": custom_user}
    return render(request, 'Contact.html', context)

