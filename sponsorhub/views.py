from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import ForbesList
from .forms import ContactForm


def homepage(request):
    forbes_lists = ForbesList.objects.all()
    return render(request, 'homepage.html', {'forbes_lists': forbes_lists})


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ContactForm(request.POST)

    return render(request, 'Contact.html', {'form': form})

