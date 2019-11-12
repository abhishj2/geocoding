import folium
import pandas

data=pandas.read_csv('india_cities.csv',encoding="ISO-8859-1")
lat=list(data["Latitude"])
lon=list(data["Longitude"])
name=list(data["City"])
SNo=list(data["SNo"])

def color_producer(SNo):
	if SNo<11:
		return 'green'
	elif 11<= SNo<22:
		return 'red'
	else:
		return 'blue'
map=folium.Map(location=[22.5,84.2],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Cities")
for lt,ln,nm,sn in zip(lat,lon,name,SNo): 
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=nm,
    fill_color=color_producer(sn),color='grey',fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")