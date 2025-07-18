document.addEventListener("DOMContentLoaded", function () {
    const calendarEl = document.getElementById("calendar");
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        locale: "es",
        events: [
            { title: "Noche de Oración", start: "2025-02-20" },
            { title: "Encuentro Juvenil", start: "2025-03-05" },
            { title: "Conferencia Bíblica", start: "2025-04-10" },
            { title: "Tarde de Alabanza", start: "2025-02-25" },
            { title: "Servicio Especial", start: "2025-05-15" }
        ]
    });
    calendar.render();
});
