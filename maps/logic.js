// Creating map object
let myMap = L.map("map", {
  center: [36.1627, -86.7816],
  zoom: 4
});


// Adding tile layer
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: 'mapbox/light-v9',  
  accessToken: API_KEY
}).addTo(myMap);

// Load in  data
var geoData = "../static/basegeo.json";

var geojson;

// Grab data with d3
d3.json(geoData, function(data) {

  // Create a new choropleth layer
  geojson = L.choropleth(data, {

    // Define what  property in the features to use*****-this may be where we would add year
    valueProperty: "per10000",

    // Set color scale
    scale: ["#ffffb2", "#b10026"],

    // Number of breaks in step range
    steps: 10,

    // q for quartile, e for equidistant, k for k-means
    mode: "q",
    style: {
      // Border color
      color: "#fff",
      weight: .3,
      fillOpacity: 0.8
    },

    // Binding a pop-up to each layer
    onEachFeature: function(feature, layer) {
      layer.bindPopup("State : " + feature.properties.State + "<br>Number of transfers : " + feature.properties.per10000);
    }
  }).addTo(myMap);

  // Set up the legend
  var legend = L.control({ position: "bottomright" });
  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");
    var limits = geojson.options.limits;
    var colors = geojson.options.colors;
    var labels = [];

    // Add min & max
    var legendInfo = "<h1>1033 Transfers<br>per 10000 residents</h1>" +
      "<div class=\"labels\">" +
        "<div class=\"min\">" + limits[0]*100 + "</div>" +
        "<div class=\"max\">" + limits[limits.length - 1]*100
         + "</div>" + "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function(limit, index) {
      labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;
  };

  legend.addTo(myMap);
      
});


  // var sliderControl = L.control.sliderControl({layer:layer, follow: 1});
  //   map.addControl(sliderControl);
  //   sliderControl.startSlider();
