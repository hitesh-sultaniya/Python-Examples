import folium
import pandas

markerData = pandas.read_csv("Volcanoes_USA.txt")

latitudeList = list(markerData["LAT"])
longitudeList = list(markerData["LON"])
elevationList = list(markerData["ELEV"])

def colorProducer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[23.0225,72.5714],zoom_start=10,tiles="Mapbox Bright")
featureGroup=folium.FeatureGroup(name="Web Map")

for lat,lon,elevation in zip(latitudeList,longitudeList,elevationList):
    featureGroup.add_child(folium.CircleMarker(location=[lat, lon], radius = 10, popup=str(elevation)+" m",
    fill_color=colorProducer(elevation), fill=True,  color = 'grey', fill_opacity=0.7))


map.add_child(featureGroup)
map.save("WebMap.html")
