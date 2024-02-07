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
