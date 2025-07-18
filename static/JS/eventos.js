document.addEventListener('DOMContentLoaded', function() {
    // Inicializar calendario
    const calendarEl = document.getElementById('calendar');
    if (calendarEl) {
        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            locale: 'es',
            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
            events: '/api/eventos',
            eventClick: function(info) {
                const eventData = info.event.extendedProps;
                const eventDetails = `
                    <h3>${info.event.title}</h3>
                    <p><strong>Lugar:</strong> ${eventData.location || 'No especificado'}</p>
                    <p><strong>Fecha:</strong> ${info.event.start.toLocaleDateString()}</p>
                    <p><strong>Hora:</strong> ${info.event.start.toLocaleTimeString()} - ${info.event.end.toLocaleTimeString()}</p>
                    <p><strong>Descripción:</strong> ${eventData.description || 'No hay descripción'}</p>
                `;
                
                // Puedes usar SweetAlert o alert estándar
                alert(eventDetails.replace(/<[^>]*>/g, ''));
            }
        });
        calendar.render();
    }

    // Funcionalidad para añadir eventos (solo master)
    if (document.getElementById('abrirModalEvento')) {
        const modal = document.getElementById('modalEvento');
        const btnAbrir = document.getElementById('abrirModalEvento');
        const btnCerrar = document.querySelector('.close-modal');
        const formEvento = document.getElementById('formEvento');
        
        btnAbrir.addEventListener('click', () => modal.style.display = 'block');
        btnCerrar.addEventListener('click', () => modal.style.display = 'none');
        window.addEventListener('click', (e) => e.target === modal ? modal.style.display = 'none' : null);
        
        formEvento.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const submitBtn = formEvento.querySelector('button[type="submit"]');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Guardando...';
            
            try {
                const formData = new FormData(formEvento);
                formData.append('destacado', formEvento.querySelector('#eventoDestacado').checked ? '1' : '0');
                
                const response = await fetch('/eventos_añadir', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) throw new Error(await response.text());
                
                const data = await response.json();
                if (data.success) {
                    alert('Evento creado exitosamente');
                    modal.style.display = 'none';
                    window.location.reload();
                } else {
                    throw new Error(data.message || 'Error al crear evento');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error: ' + error.message);
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<i class="fas fa-calendar-plus"></i> Crear Evento';
            }
        });
    }
});