$(document).ready(function () {
  $('#btn_translate').click(translateHello);

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();
    const helloLink = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
    $.get(helloLink, function (data) {
      $('#hello').text(data.hello);
    });
  }
});
