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

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
featureGroupVolcanoes=folium.FeatureGroup(name="Volcanoes")

for lat,lon,elevation in zip(latitudeList,longitudeList,elevationList):
    featureGroupVolcanoes.add_child(folium.CircleMarker(location=[lat, lon], radius = 6, popup=str(elevation)+" m",
    fill_color=colorProducer(elevation), fill=True,  color = 'grey', fill_opacity=0.7))

featureGroupPopulation=folium.FeatureGroup(name="Population")
featureGroupPopulation.add_child(folium.GeoJson(data=(open("world.json",'r',encoding="utf-8-sig")).read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(featureGroupVolcanoes)
map.add_child(featureGroupPopulation)
map.add_child(folium.LayerControl())
map.save("WebMap.html")
