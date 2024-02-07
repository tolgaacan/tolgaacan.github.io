document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.content').classList.add('fade-in');
});

window.addEventListener('DOMContentLoaded', setup);

function setup() {
    const h1Elements = document.querySelectorAll('h1');

    const options = {
        root: null,
        threshold: 0,
        rootMargin: "0px 0px -200px 0px"
    }

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('underline');
                observer.unobserve(entry.target);
            }
        })
    }, options);

    h1Elements.forEach(h1 => {
        observer.observe(h1);
    })
}

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("image-container")[0].getElementsByTagName("img");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

