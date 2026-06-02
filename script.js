document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Logic
    const mobileBtn = document.querySelector('.mobile-toggle');
    const mobileMenu = document.getElementById('mobileMenu');

    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('show');
            const icon = mobileBtn.querySelector('i');
            if (mobileMenu.classList.contains('show')) {
                icon.classList.replace('fa-bars', 'fa-times');
            } else {
                icon.classList.replace('fa-times', 'fa-bars');
            }
        });
    }
});
