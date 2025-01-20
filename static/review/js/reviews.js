document.addEventListener('DOMContentLoaded', function() {
    // Handle star filter buttons
    const starFilters = document.querySelectorAll('.star-filter');
    starFilters.forEach(button => {
        button.addEventListener('click', function() {
            starFilters.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            // Add filter logic here
        });
    });

    // Handle helpful/not helpful buttons
    const helpfulBtns = document.querySelectorAll('.helpful-btn, .not-helpful-btn');
    helpfulBtns.forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('clicked')) {
                this.classList.add('clicked');
                const count = this.textContent.match(/\d+/);
                const newCount = parseInt(count) + 1;
                this.innerHTML = this.innerHTML.replace(/\d+/, newCount);
                
                // Add animation
                this.style.transform = 'scale(1.1)';
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 200);
            }
        });
    });

    // Handle sort select
    const sortSelect = document.getElementById('sort-reviews');
    sortSelect.addEventListener('change', function() {
        // Add sorting logic here
    });

    // Handle load more button
    const loadMoreBtn = document.getElementById('load-more-btn');
    loadMoreBtn.addEventListener('click', function() {
        // Simulate loading with animation
        this.innerHTML = 'Loading...';
        this.style.opacity = '0.7';
        
        setTimeout(() => {
            // Add more reviews here
            this.innerHTML = 'Load More Reviews';
            this.style.opacity = '1';
        }, 1000);
    });

    // Add smooth scroll animation for new reviews
    function addSmoothScroll() {
        document.querySelectorAll('.review-card').forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                card.style.transition = 'opacity 0.5s, transform 0.5s';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 100);
        });
    }

    // Call initially
    addSmoothScroll();
});
