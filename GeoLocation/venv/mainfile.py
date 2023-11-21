import program
program.main()

import folium
m = folium.Map(
    location=[45.5236, -122.6750],
    tiles='Syracuse',
    zoom_start=13,
    API_key='AIzaSyADySfAiLC9qj4gwpAY40Fs5B2mBBbwlfE'
)

import createCsv


data = next(read_csv(), None)
x=0
while data is not None:
    folium.Circle(
        radius=100,
        location=[45.5244, -122.6699],
        popup=data[x][3],
        color='crimson',
        fill=False,
    ).add_to(m)
    folium.CircleMarker(
        location=[45.5215, -122.6261],
        radius=50,
        popup='Laurelhurst Park',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)

#display
m

