const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(url, (data) => {
  $('#hello').append(data.hello);
});
