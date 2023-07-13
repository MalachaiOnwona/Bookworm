from pathlib import Path
import json
import plotly.express as px

path = Path('C:\Users\Malachai Onwona\Python Crash Course Book Projects\Downloading Data\earthquake_data\eq_data_30_day_m1.geojson')
contents = path.read_text()
eq_data = json.loads(contents)

eq_dicts = eq_data['features']

magnitudes, longitudes, latitudes, eq_titles = [], [], [], []
for eq_dict in eq_dicts:
    magnitude = eq_dict['properties']['mag']
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)
    eq_titles.append(eq_title)

print(magnitudes[:10])
print(longitudes[:5])
print(latitudes)[:5]

figure = px.scatter_geo(lat= latitudes, lon= longitudes, size= magnitudes, title= 'Global Earthquakes',
                        color= magnitudes, color_continuous_scale= 'Viridis', 
                        labels= {'color': 'Magnitude'}, projection= 'natural earth',
                        hover_name= eq_titles)

figure.show()

path = Path('earthquake_data/readable_eq_data.geojson')
readable_contents = json.dumps(eq_data, indent=4)
path.write_text(readable_contents)