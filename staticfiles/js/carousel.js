document.addEventListener('DOMContentLoaded', () => {
    const carouselElement = document.getElementById('postFormCarousel');
    if (carouselElement) {
        const stepsButton = document.getElementById('stepsButton');
        const totalSteps = document.querySelectorAll('.carousel-item').length;

        const updateStepsButton = () => {
            const activeSlideIndex = Array.from(carouselElement.querySelectorAll('.carousel-item')).indexOf(carouselElement.querySelector('.carousel-item.active'));
            stepsButton.textContent = `Step ${activeSlideIndex + 1} of ${totalSteps}`;
        };

        carouselElement.addEventListener('slid.bs.carousel', updateStepsButton);

        updateStepsButton();
    }
});