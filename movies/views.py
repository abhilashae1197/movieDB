from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import MovieForm
from .models import Movies
from .serializers import MovieSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, get_object_or_404


# Create your views here.


class MovieListCreateAPI(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    renderer_classes = [TemplateHTMLRenderer]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get(self, request, *args, **kwargs):
        return Response({'movies': self.get_queryset()}, template_name='movie_list.html')


class MovieCreateReterieveUpdateAPI(APIView):
    serializer_class = MovieSerializer

    # renderer_classes = [TemplateHTMLRenderer]

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^name', 'cast', 'director', 'genre']
    # def get(self, request, pk=None, *args, **kwargs):
    #     mov = Movies.objects.get(id=pk)
    #     serializer = MovieSerializer()
    #     return Response({}, status=status.HTTP_200_OK)
    def get(self, request, *args, **kwargs):
        if not 'pk' in kwargs:
            queryset = Movies.objects.all()
            return Response(MovieSerializer(queryset, many=True).data, status=status.HTTP_200_OK)
        q = Movies.objects.filter(id=kwargs['pk']).last()
        return Response(MovieSerializer(q).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        mov = Movies.objects.get(id=pk)
        serializer = MovieSerializer(mov, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movie_add.html'

    def get(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return redirect('movie_list')

    # def get(self, request, pk):
    #     movie = get_object_or_404(Movies, pk=pk)
    #     serializer = MovieSerializer(movie)
    #     return Response({'serializer': serializer, 'movie': movie})
    #
    # def post(self, request, pk):
    #     movie = get_object_or_404(Movies, pk=pk)
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'movie': movie})
    #         serializer.save()
    #         return redirect('movie_list')



class MovieRetrieveUpdateAPI(RetrieveUpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^name', 'cast', 'directed_by', 'genre']


class MovieFormView(CreateView):
    template_name = 'movie_add.html'
    form_class = MovieForm
    success_url = '/movie/MovieLCapi/'
    model = Movies

    def post(self, request, *args, **kwargs):
        form = MovieForm(request.POST)
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        return Response(status=status.HTTP_400_BAD_REQUEST)