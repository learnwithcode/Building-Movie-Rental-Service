from django.shortcuts import render
from django.views.generics import ListView
from core.models import Movie

class MovieList(ListView):
	model = Movie