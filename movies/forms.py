from django import forms
from rest_framework.exceptions import ValidationError

from movies.models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('name', 'year', 'runtime', 'cast', 'genre', 'director', 'producer', 'imdb_rating', 'imdb_url', 'thumbnail_url')

        # def clean_file(self, form):
        #     if form.is_valid():
        #         raise ValidationError("Invalid form")