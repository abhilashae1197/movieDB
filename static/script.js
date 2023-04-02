$('#btn').click(function() {

  $.ajax({
    type : 'GET',
    data : {
      datas : $('#movie_title').val()
    },
    success : function(response) {
      var message = response.message

      window.location.href = '/movie/movie-info' + '?title=' + $('#movie_title').val()
    }

  });
});


$('#save-btn').click(function() {

  $.ajax({
    url : 'https://www.omdbapi.com?apikey=34c6a316&t=' + $('#title').text().replace("Title:", "").trim(),
    type : 'GET',
    success : function(response) {

    $.ajax({
    url : '/movie/movie/',
    type : 'POST',
    data : {
      'name': response['Title'],
      'runtime': response['Runtime'],
      'year': response['Year'],
      'cast': response['Actors'],
      'genre': response['Genre'],
      'director': response['Director'],
      'producer': response['Production'],
      'imdb_rating': response['imdbRating'],
      'imdb_url': 'https://www.imdb.com/title/' + response['imdbID'],
      'thumbnail_url': response['Poster'],
//      'csrfmiddlewaretoken': 'x3GL1CdukoOMg8eWnpeoVyJ1GuG8DIJZgvVOtagbOTBFZZIKJIx1WRNSUGn7Eogm'
    },
    success : function(response) {
      window.location.href = '/movie/movie-list'
    }

  });
    }

  });
});

$('#search-btn').click(function() {

  $.ajax({
    type : 'GET',
    success : function(response) {
      var message = response.message

      window.location.href = '/movie/movie-list?' + $('#type').val() + '=' + $('#type_val').val()
    }

  });
});