from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import ForbesList


def homepage(request):
    return render(request, 'homepage.html')


def scrapeandsave(request):
    url = "https://www.forbes.com/forbes-400/"
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')

    #Scraping the data
    for person in soup.find_all('div', {'class': 'Table_tableRow__M82uU'})[:16]:

        rank = person.find('div', {'class': 'Table_rank__KnjUY'}).text
        name = person.find('div', {'class': 'Table_personName__UO41W'}).text
        net_worth = person.find('div', {'class': 'Table_netWorth__py4xM'}).text
        age = person.find('div', {'class': 'Table_age__CHhfQ'}).text

        #Saving the data in DB
        forbes_list = ForbesList(rank=rank, name=name, net_worth=net_worth, age=age)
        forbes_list.save()

    return render(request, 'homepage.html')
