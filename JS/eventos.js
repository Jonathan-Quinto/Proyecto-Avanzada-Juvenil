document.addEventListener("DOMContentLoaded", function () {
    const eventos = [
        { nombre: "Noche de Oración", fecha: "2025-02-20", hora: "19:00", lugar: "Templo Central" },
        { nombre: "Encuentro Juvenil", fecha: "2025-03-05", hora: "17:00", lugar: "Salón de Eventos" },
        { nombre: "Conferencia Bíblica", fecha: "2025-04-10", hora: "18:30", lugar: "Auditorio Principal" },
        { nombre: "Tarde de Alabanza", fecha: "2025-02-25", hora: "16:00", lugar: "Templo Central" },
        { nombre: "Servicio Especial", fecha: "2025-05-15", hora: "10:00", lugar: "Templo Central" }
    ];

    const eventosContainer = document.querySelector(".eventos-container");
    const hoy = new Date();

    // Filtra los eventos más cercanos
    const eventosProximos = eventos.filter(evento => new Date(evento.fecha) >= hoy)
                                   .sort((a, b) => new Date(a.fecha) - new Date(b.fecha))
                                   .slice(0, 3); // Muestra solo los 3 más cercanos

    // Inserta los eventos en la página
    eventosProximos.forEach(evento => {
        const eventoHTML = `
            <div class="evento">
                <h3>${evento.nombre}</h3>
                <p><strong>Fecha:</strong> ${evento.fecha}</p>
                <p><strong>Hora:</strong> ${evento.hora}</p>
                <p><strong>Lugar:</strong> ${evento.lugar}</p>
            </div>
        `;
        eventosContainer.innerHTML += eventoHTML;
    });
});
