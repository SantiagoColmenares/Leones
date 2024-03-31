function myFunction() {
  let x = document.getElementById("myNavbar");
  if (x.className === "navbar") {
    x.className += " responsive";
  } else {
    x.className = "navbar";
  }
}


const overlayBtns = document.querySelectorAll('.overlay-btn');

overlayBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    btn.classList.toggle('active');
    btn.closest('.card').querySelector('.overlay').classList.toggle('active');
  });
});