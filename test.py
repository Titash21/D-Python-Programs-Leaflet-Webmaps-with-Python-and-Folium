import  folium
import pandas
#main object of folium is a map object
dataframe=pandas.read_csv("Volcanoes-USA.txt",sep=",")
map=folium.Map(
               location=[dataframe["LAT"].mean(),dataframe["LON"].mean()],
               zoom_start=7,
               tiles='Stamen Terrain'
               )
folium.Marker(
                location=[45.3288,-121.6625],
                popup='Mt. Hood Meadows',
                icon=folium.Icon(color='red')
             ).add_to(map)


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

for lat,lon ,name, elevation in zip(dataframe["LAT"],dataframe["LON"],dataframe["NAME"],dataframe["ELEV"]):
    map.add_child(folium.Marker(
                    location=[lat,lon],
                    popup=name,
                    icon=folium.Icon(color=color_of_marker(elevation),icon_color='black')
                 ))


print("Marking in the Map  ", map)
map.save('Mapping.html')
