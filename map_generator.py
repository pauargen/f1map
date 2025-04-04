import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os
import matplotlib.pyplot as plt
import folium
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import json

df = pd.read_csv('circuits.csv') 

# Load GeoJSON data
with open('f1-circuits.geojson') as f:
    geojson_data = json.load(f)

colors = list(mcolors.TABLEAU_COLORS.values())

# Create dark map
m = folium.Map(location=[df['lat'].mean(), df['lng'].mean()], 
                zoom_start=2, 
                tiles='CartoDB dark_matter',  
                max_zoom=15,  
                min_zoom=2)  

#F1 colored circuit
for i, (_, row) in enumerate(df.iterrows()):
    color = colors[i % len(colors)]  
    popup_content = f'''
        <div style="font-family: 'Arial', sans-serif; color: black; font-size: 12px;">
            <strong>{row['name']}</strong>
        </div>
    '''
    folium.CircleMarker(
        location=[row['lat'], row['lng']],
        radius=8,  
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.8,  
        weight=0,  
        popup=folium.Popup(popup_content, max_width=200)  
    ).add_to(m)

def style_function(feature):
    return {
        'fillColor': 'white',  
        'color': 'white',        
        'weight': 3,           
        'fillOpacity': 1        
    }

folium.GeoJson(
    geojson_data,
    tooltip=folium.GeoJsonTooltip(
        fields=['Name'],
        aliases=['Circuit:'],
        localize=True,
    ),
    style_function=style_function
).add_to(m)

m.save('f1_circuits_highlight.html')
