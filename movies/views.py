from django.contrib.sites import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import FormView, CreateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .forms import MovieForm, MovieImdbForm
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, get_object_or_404
import requests


# Create your views here.


class MovieListCreateAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    renderer_classes = [TemplateHTMLRenderer]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get(self, request, *args, **kwargs):
        return Response({'movies': self.get_queryset()}, template_name='movie_list.html')

    def get_queryset(self):
        queryset = Movie.objects.all()
        name = self.request.query_params.get('name')
        director = self.request.query_params.get('director')
        cast = self.request.query_params.get('cast')
        genre = self.request.query_params.get('genre')
        if name is not None:
            queryset = Movie.objects.filter(name__icontains=name)
        elif director is not None:
            queryset = Movie.objects.filter(director__icontains=director)
        elif cast is not None:
            queryset = Movie.objects.filter(cast__icontains=cast)
        elif genre is not None :
            queryset = Movie.objects.filter(genre__icontains=genre)
        return queryset


class MovieCreateReterieveUpdateAPIView(APIView):
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        if not 'pk' in kwargs:
            queryset = Movie.objects.all()
            return Response(MovieSerializer(queryset, many=True).data, status=status.HTTP_200_OK)
        q = Movie.objects.filter(id=kwargs['pk']).last()
        return Response(MovieSerializer(q).data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        mov = Movie.objects.get(id=pk)
        serializer = MovieSerializer(mov, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MovieRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieFormView(CreateView):
    template_name = 'movie_add.html'
    form_class = MovieForm
    success_url = '/movie/movie-list/'
    model = Movie

    def post(self, request, *args, **kwargs):
        form = MovieForm(request.POST)
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def movie_imdb_form(req):
    return render(req, "movie_imdb.html")


def movie_info(req):
    title = req.GET['title']
    response = requests.get('https://www.omdbapi.com/', params={'apikey': '34c6a316', 't': title})
    res = response.json()

    template = loader.get_template('movie_info.html')
    context = {
        'info': res,
    }
    return HttpResponse(template.render(context, req))
