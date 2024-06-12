// js pra usar em celular
window.addEventListener('DOMContentLoaded', function() {
    if (window.innerWidth <= 767) {
        // por algum motivo isso nao funfa 🤡
        const newsContainers = document.querySelectorAll('.news-container');
        newsContainers.forEach(container => {
            new Glider(container, {
                slidesToShow: 'auto',
                slidesToScroll: 'auto',
                dots: '.dots',
                arrows: {
                    prev: '.glider-prev',
                    next: '.glider-next'
                },
                draggable: true,
                responsive: [
                    {
                        breakpoint: 768,
                        settings: {
                            slidesToShow: 1,
                            slidesToScroll: 1,
                        }
                    }
                ]
            });
        });
    }
});
