from django.template import RequestContext
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .models import Film
from django.db.models import Q
import random


def index(request):
    all_films = Film.objects.all().order_by('tytul')
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'all_films': all_films,
        'gatunki': gatunki
    }
    return render(request, 'film/index.html', context)


class DetailView(generic.DetailView):
    model = Film
    template_name = 'film/detail.html'


def dysk_view(request):
    dysk_films = Film.objects.filter(gdzie='Dysk')
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'dysk_films': dysk_films,
        'gatunki': gatunki,
    }

    return render(request, 'film/dysk.html', context)


def netflix_view(request):
    netflix_films = Film.objects.filter(gdzie="Netflix")
    gatunki = Film.objects.all().order_by('gatunek')

    context = {
        'netflix_films': netflix_films,
        'gatunki': gatunki,
    }

    return render(request, 'film/netflix.html', context)


class FilmCreate(generic.CreateView):
    model = Film
    fields = ['tytul', 'gatunek', 'gatunek2', 'gatunek3', 'rok', 'nota', 'gdzie']


class FilmUpdate(generic.UpdateView):
    model = Film
    fields = ['tytul', 'gatunek', 'gatunek2', 'gatunek3', 'rok', 'nota', 'gdzie']


class FilmDelete(generic.DeleteView):
    model = Film
    success_url = reverse_lazy('film:index')


def searching_all(request):
    query = request.GET.get('q')
    film_search = Film.objects.filter(tytul__contains=query)
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'film_search': film_search,
        'gatunki': gatunki,
    }
    return render(request, 'film/index.html', context)


def searching_dysk(request):
    query = request.GET.get('q')
    film_search = Film.objects.filter(Q(gdzie='Dysk') & Q(tytul__contains=query))
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'film_search': film_search,
        'gatunki': gatunki,
    }
    return render(request, 'film/dysk.html', context)


def searching_netflix(request):
    query = request.GET.get('q')
    film_search = Film.objects.filter(Q(gdzie='Netflix') & Q(tytul__contains=query))
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'film_search': film_search,
        'gatunki': gatunki,
    }
    return render(request, 'film/netflix.html', context)


def filtering_gatunek_all(request, genre):
    film_filter = Film.objects.filter(gatunek=genre)
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'film_filter': film_filter,
        'gatunki': gatunki,
    }
    return render(request, 'film/index.html', context)


def filtering_gatunek_dysk(request, genre):
    film_filter = Film.objects.filter(gatunek=genre)
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'film_filter': film_filter,
        'gatunki': gatunki,
    }
    return render(request, 'film/dysk.html', context)


def filtering_gatunek_netflix(request, genre):
    film_filter = Film.objects.filter(gatunek=genre)
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'film_filter': film_filter,
        'gatunki': gatunki,
    }
    return render(request, 'film/netflix.html', context)


def filtering_nota_all(request):
    result = request.GET.get('notaRange')
    nota_filter = Film.objects.filter(nota__gte=result)
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'nota_filter': nota_filter,
        'gatunki': gatunki,
    }
    return render(request, 'film/index.html', context)


def filtering_nota_dysk(request):
    result = request.GET.get('notaRange')
    nota_filter = Film.objects.filter(Q(gdzie="Dysk") & Q(nota__gte=result))
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'nota_filter': nota_filter,
        'gatunki': gatunki,
    }
    return render(request, 'film/dysk.html', context)


def filtering_nota_netflix(request):
    result = request.GET.get('q')
    nota_filter = Film.objects.filter(nota__gte=result)
    gatunki = Film.objects.all().order_by('gatunek')
    context = {
        'nota_filter': nota_filter,
        'gatunki': gatunki,
    }
    return render(request, 'film/netflix.html', context)


def drawing(request):
    draw = Film.objects.all().order_by('?')[0]
    return render(request, 'film/drawing.html', {'draw': draw})