// JavaScript for initializing sliders on phones
window.addEventListener('DOMContentLoaded', function() {
    // Check if the device screen width is less than or equal to 767 pixels (phone width)
    if (window.innerWidth <= 767) {
        // Initialize sliders for each company's news
        const newsContainers = document.querySelectorAll('.news-container');
        newsContainers.forEach(container => {
            // Initialize slider for each company's news inside the container
            new Glider(container, {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: '.dots',
                arrows: {
                    prev: '.glider-prev',
                    next: '.glider-next'
                }
            });
        });
    }
});
