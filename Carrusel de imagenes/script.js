let currentIndex = 0;
const images = document.querySelectorAll('.carousel-images img');

function showSlide(index) {
    images[currentIndex].classList.remove('active');
    currentIndex = (index + images.length) % images.length;
    images[currentIndex].classList.add('active');
}

function nextSlide() {
    showSlide(currentIndex + 1);
}

function prevSlide() {
    showSlide(currentIndex - 1);
}

// Automáticamente cambia de imagen cada 3 segundos
setInterval(nextSlide, 3000);
