import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    stations_list = []

    with open (BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            station_dict = {
                'Name': row.get('Name'),
                'Street': row.get('Street'),
                'District': row.get('District')
            }
            stations_list.append(station_dict)

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_num)

    context = {
       'bus_stations': stations_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
