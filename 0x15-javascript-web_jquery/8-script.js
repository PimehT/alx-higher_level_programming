const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data) {
  data.results.forEach(film => {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  });
});
