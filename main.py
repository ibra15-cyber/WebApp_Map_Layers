import folium

#making a map object using folium
#passing lat and log as a list to location parameter
map = folium.Map(location=[80, -100], zoom_start=6, titles="Name of the Place")

#save our map as Map1.html
map.save("Map1.html")
