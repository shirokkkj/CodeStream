document.querySelectorAll('input, select, textarea').forEach(element => {
    element.addEventListener('focus', () => {
        element.style.transform = 'scale(1.02)';
    });
    element.addEventListener('blur', () => {
        element.style.transform = 'scale(1)';
    });
});


