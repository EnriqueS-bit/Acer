function initMap() {
    // Coordenadas del río Guatapurí en Valledupar, Colombia
    var guatapuri = { lat: 10.4833, lng: -73.25 };

    // Crear el mapa centrado en el río Guatapurí
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: guatapuri
    });

    // Añadir un marcador en el río Guatapurí
    var marker = new google.maps.Marker({
        position: guatapuri,
        map: map,
        title: 'Río Guatapurí'
    });

    // Añadir un evento de clic para agregar nuevos marcadores
    map.addListener('click', function(event) {
        addMarker(event.latLng, map);
    });
}

// Función para añadir un nuevo marcador
function addMarker(location, map) {
    new google.maps.Marker({
        position: location,
        map: map
    });
}
