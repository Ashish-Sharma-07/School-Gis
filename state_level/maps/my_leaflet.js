/////////////////////////////////////schools////////////////////////////////////////////////
var feature = base;
///////////////color selector////////////////////////////
function getColor_school(d) {
        color = ['#800026','#BD0026','#E31A1C','#FC4E2A','#FD8D3C','#FFEDA0'];
        range = 5875;
        grade = [Math.round(range*0.2,2),Math.round(range*0.4,2),Math.round(range*0.6,2),Math.round(range*0.8,2),,Math.round(range*1,2)];
        for(i=0;i<color.length-1;i++){
            if(d < grade[i]){
            return color[i];
                }
            }
	    return color[i];
	    }

function getColor_teacher(d) {
        color = ['#800026','#BD0026','#E31A1C','#FC4E2A','#FD8D3C','#FFEDA0'];
        range = 6937;
        grade = [Math.round(range*0.2,2),Math.round(range*0.4,2),Math.round(range*0.6,2),Math.round(range*0.8,2),,Math.round(range*1,2)];
        for(i=0;i<color.length-1;i++){
            if(d < grade[i]){
            return color[i];
                }
            }
	    return color[i];
	    }

function getColor_student(d) {
        color = ['#800026','#BD0026','#E31A1C','#FC4E2A','#FD8D3C','#FFEDA0'];
        range = 197578;
        grade = [Math.round(range*0.2,2),Math.round(range*0.4,2),Math.round(range*0.6,2),Math.round(range*0.8,2),,Math.round(range*1,2)];
        for(i=0;i<color.length-1;i++){
            if(d < grade[i]){
            return color[i];
                }
            }
	    return color[i];
	    }

function getColor_security(d) {
        //['bndrywall_1','bndrywall_2','bndrywall_3','bndrywall_4','bndrywall_5','bndrywall_6','bndrywall_7','bndrywall_8']
        weights = [0.1, 0.6, 0.4, 0.8, 0.7, 0, 0.3, 0.5, 0.2]
        g_w = d.
        color = ['#800026','#BD0026','#E31A1C','#FC4E2A','#FD8D3C','#FFEDA0'];
        range = 197578;
        grade = [Math.round(range*0.2,2),Math.round(range*0.4,2),Math.round(range*0.6,2),Math.round(range*0.8,2),,Math.round(range*1,2)];
        for(i=0;i<color.length-1;i++){
            if(d < grade[i]){
            return color[i];
                }
            }
	    return color[i];
	    }


var school = function(){
    //map.eachLayer(function(){map.removeLayer();});
    function style(feature) {
        return {
	    weight: 2,
	    opacity: 1,
	    color: 'white',
	    dashArray: '3',
	    fillOpacity: 0.7,
	    fillColor: getColor(feature.properties.schools)
	    };
    }
    function onEachFeature(feature, layer) {
	layer.on({
		mouseover: highlightFeature,
		mouseout: resetHighlight,
		click: zoomToFeature
	});}

    function resetHighlight(e) {
	    geojson.resetStyle(e.target);
	//  info.update();
    }

    function zoomToFeature(e) {
	map.fitBounds(e.target.getBounds());
    }

    function highlightFeature(e) {
	var layer = e.target;
	layer.setStyle({
		weight: 5,
		color: '#666',
		dashArray: '',
		fillOpacity: 0.7
	});
	if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
		layer.bringToFront();}
		info.update(layer.feature.properties.school);
    }

    var school_map = L.geoJson(data,{style: style,onEachFeature: onEachFeature,}).addTo(map);

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = grade;
        labels = [];
    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<span style="width:10px;background-color:' + getColor(grades[i] + 1) + '"></span> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
    return div;
    };
    legend.addTo(map);
}
/////////////////////////////////////////////Teacher//////////////////////////////////////////////////////////
var teacher = function(){
    //map.eachLayer(function(){map.removeLayer();});
    function getColor(d) {
        color = ['#800026','#BD0026','#E31A1C','#FC4E2A','#FD8D3C','#FFEDA0'];
        range = 6937;
        grade = [Math.round(range*0.2,2),Math.round(range*0.4,2),Math.round(range*0.6,2),Math.round(range*0.8,2),Math.round(range*1,2)];
        for(i=0;i<color.length-1;i++)
        {
            if(d < grade[i]){
            return color[i];}
            }
	    return color[i];
	    }

    function style(feature) {
        return {
	    weight: 2,
	    opacity: 1,
	    color: 'white',
	    dashArray: '3',
	    fillOpacity: 0.7,
	    fillColor: getColor(feature.properties.teacher)
	    };
    }

    function onEachFeature(feature, layer) {
	layer.on({
		mouseover: highlightFeature,
		mouseout: resetHighlight,
		click: zoomToFeature
	});}

    function resetHighlight(e) {
	    geojson.resetStyle(e.target);
	//  info.update();
    }

    function zoomToFeature(e) {
	map.fitBounds(e.target.getBounds());
    }

    function highlightFeature(e) {
	var layer = e.target;
	layer.setStyle({
		weight: 5,
		color: '#666',
		dashArray: '',
		fillOpacity: 0.7
	});
	if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
		layer.bringToFront();}
		info.update(layer.feature.properties.teacher);
    }

    var school_map = L.geoJson(data,{style: style,onEachFeature: onEachFeature,}).addTo(map);

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = grade;
        labels = [];
    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<span style="width:10px;background-color:' + getColor(grades[i] + 1) + '"></span> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
    return div;
    };
    legend.addTo(map);
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////