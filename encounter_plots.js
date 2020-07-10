function unpack(rows, index) {
    return rows.map(function(row) {
        return row[index];
    });
};

function getData() {
    d3.json(/* database/encounters_table */).then(function(data) {
        var state = unpack(/* state data, index */);
        var age = unpack(/* age data, index */);
        var gender = unpack(/* gender data, index */);
        var race = unpack(/* race data, index */);
        var city = unpack(/* city data */);
        var lat = unpack(/* latitude data */);
        var long = unpack(/* longitude data */);
        var mental_illness = unpack(/* mental illness data */);
        var year = unpack(/* year */);

        buildPlot(/* table.length, state */);
    })
}

function buildPlot() {
    d3.json(/* database/encounters_table */).then(function(data) {
        var state = unpack(/* state data, index */);
        var age = unpack(/* age data, index */);
        var gender = unpack(/* gender data, index */);
        var race = unpack(/* race data, index */);
        var city = unpack(/* city data */);
        var lat = unpack(/* latitude data */);
        var long = unpack(/* longitude data */);
        var mental_illness = unpack(/* mental illness data */);
        var year = unpack(/* year */);

        getData();

        var trace = {
            type: "bar",
            name: /* data name? */,
            x: /* data to plot */,
            y: /* encounters.length */,
        }

        var data = [trace];

        var layout = {
            title: "",
            
        }
    })
}