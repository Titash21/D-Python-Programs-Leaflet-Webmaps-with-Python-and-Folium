import  folium
#main object of folium is a map object
map=folium.Map(location=[45.372,-121.697],zoom_start=12,tiles='Stamen Terrain')
print(map)
map.save('testMap.html')
