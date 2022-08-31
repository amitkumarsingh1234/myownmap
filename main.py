import folium
map=folium.Map(location=[22.05104912165626, 88.07211951548017],zoom_start=15)
folium.CircleMarker(location=[22.05104912165626, 88.07211951548017],radius=50,popup = "anyplace").add_to(map)
folium.Marker([22.05104912165626, 88.07211951548017],popup="unknown place").add_to(map)
folium.Marker([22.05216284734576, 88.07495192801487],popup="place").add_to(map)
folium.PolyLine(locations=[(22.05104912165626, 88.07211951548017),(22.05216284734576, 88.07495192801487)],line_opacity = 0.6).add_to(map)
map.save("map.html")