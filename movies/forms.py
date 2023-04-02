from django import forms
from rest_framework.exceptions import ValidationError

from movies.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
        'name', 'year', 'runtime', 'cast', 'genre', 'director', 'producer', 'imdb_rating', 'imdb_url', 'thumbnail_url')


class MovieImdbForm(forms.Form):
    title = forms.CharField()

