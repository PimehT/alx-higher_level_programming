const clicker = document.querySelector('#red_header');

clicker.addEventListener('click', changeColor);

function changeColor () {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
}
