import  folium
import pandas
#main object of folium is a map object
dataframe=pandas.read_csv("Volcanoes-USA.txt",sep=",")
map=folium.Map(
               location=[dataframe["LAT"].mean(),dataframe["LON"].mean()],
               zoom_start=7,
               tiles='Stamen Terrain'
               )

#method to check the elevation of volcano and return it
def color_of_marker(elevation):

    elevation_step=int((max(dataframe["ELEV"])-min(dataframe["ELEV"]))/3)
    minimum_elevation=int(min(dataframe["ELEV"]))

    if elevation in range(minimum_elevation,minimum_elevation+elevation_step):
        color='green'
    elif elevation in range(minimum_elevation+elevation_step,minimum_elevation+2*(elevation_step)):
        color='orange'
    elif elevation in range(int(dataframe["ELEV"].mean()),int(max(dataframe["ELEV"]))):
        color='blue'
    else:
        color='red'
    return color
# Create a FeatureGroup layer - we can put things in it and handle them as a single layer.  For example, you can add a LayerControl to tick/untick the whole group.
feature_group=folium.FeatureGroup(name="Volcano Locations")
for lat,lon ,name, elevation in zip(dataframe["LAT"],dataframe["LON"],dataframe["NAME"],dataframe["ELEV"]):
    feature_group.add_child(folium.Marker(
                    location=[lat,lon],
                    popup=name,
                    icon=folium.Icon(color=color_of_marker(elevation),icon_color='black')
                 ))
    map.add_child(feature_group)


#instead of adding markers to the map , you want to to add them to to feature_group variable
map.add_child(folium.GeoJson(
                                    data=open("World_population.json"),
                                    name='World Population',
                                    style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005']<=1000000 else 'orange' if 1000000<x['properties']['POP2005']<20000000 else 'red'}
                                )
                 )
map.add_child(folium.LayerControl())

print("Marking in the Map  ", map)
map.save(outfile='testMap.html')
