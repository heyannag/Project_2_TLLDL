var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});

// var myMap = L.map("map").setView([39.8283, -98.5795], 5);

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
}).addTo(myMap);

var url = "/data";

d3.json(url).then(function(data) {
    console.log(data);

    var markers = L.markerClusterGroup();

    for(var i=0; i<data.length; i++) {

        var lat = data[i].lat;
        var lon = data[i].lon;
        // var race = data[i].race;
        // var age = data[i].age;
        // var illness = data[i].illness;

        markers.addLayer(L.marker([lat, lon])
          .bindPopup("<h3>" + data[i].race + "</h3><hr><h3> Age " + data[i].age + "</h3><hr><h4> Signs of Mental Illness: " + data[i].illness + "</h4>"));
    };

    myMap.addLayer(markers);
});