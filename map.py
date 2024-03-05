import folium

def map_coordination(file_name, lat, lon):
    area = folium.Map(location=[lat, lon], zoom_start=20)
    folium.CircleMarker(location=[lat, lon], radius=10, color='blue', fill=True, fill_color='blue').add_to(area)
    area.save(f'{file_name}.html')


map_coordination('adam', '27.886306', '34.29472')