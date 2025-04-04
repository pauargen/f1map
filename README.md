# f1map: F1 Circuits Visualization

This project visualizes Formula 1 circuit locations on an interactive map using Folium, combined with circuit data from a CSV file and GeoJSON format (source: Kaggle). The map uses a dark style for better aesthetics and highlights the circuits with different colors, providing additional information about each circuit.

## Project Overview

- **Data**: Circuit names, latitudes, and longitudes are loaded from a CSV file (`circuits.csv`).
- **GeoJSON**: Circuit boundary data is loaded from a GeoJSON file (`f1-circuits.geojson`).
- **Visualization**: The map is rendered using Folium and features:
  - A dark map background.
  - Colored markers for each circuit with popups displaying the circuit name.
  - A GeoJSON layer to display the geographical boundaries of each circuit.
  
The map is saved as an HTML file, which can be opened in any web browser.
You will have to zoom into the bubbles with white dots to appretiate the circuit's boundaries.

## Requirements

To run this project, you need to have the following Python packages installed:

- `pandas`
- `geopandas`
- `shapely`
- `os`
- `json`
- `matplotlib`
- `folium`

The resoulting map can be uplodeaded to github pages:
https://mapasf1.github.io/

![image](https://github.com/user-attachments/assets/17b66f72-a519-438c-9f8d-c9431c455b45)

After zooming in:

![image](https://github.com/user-attachments/assets/c63ad6a2-36d8-4960-8b61-153f0e4c6409)


