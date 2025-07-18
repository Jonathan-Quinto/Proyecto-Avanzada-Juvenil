document.querySelectorAll('.filtro-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const categoria = btn.dataset.categoria;
        document.querySelectorAll('.producto').forEach(producto => {
            if (categoria === 'todos' || producto.dataset.categoria === categoria) {
                producto.style.display = 'block';
            } else {
                producto.style.display = 'none';
            }
        });
        // Remover clase 'active' de todos los botones y añadirla al clickeado
        document.querySelectorAll('.filtro-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    });
});