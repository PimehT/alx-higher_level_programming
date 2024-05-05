$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const helloLink = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
    $.get(helloLink, function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      const languageCode = $('#language_code').val();
      const helloLink = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
      $.get(helloLink, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
