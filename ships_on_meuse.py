#%%
import pandas as pd
import json
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

filepath = r"D:\Projects\Detectie_graverij_data\schip_movement_ravenstein\20250618-133913-anonymous1-AIS_maas_ravenstein_202503_06.ndjson"

# Load NDJSON file
with open(filepath, 'r') as f:
    data = [json.loads(line) for line in f]

# Flatten nested fields
def extract_value(field):
    if isinstance(field, dict):
        return field.get('value') or field.get('code')
    return field

for row in data:
    row['longitude'] = extract_value(row.get('longitude'))
    row['latitude'] = extract_value(row.get('latitude'))
    row['track_id'] = extract_value(row.get('track_id'))
    row['length'] = extract_value(row.get('length'))
    row['beam'] = extract_value(row.get('beam'))
    row['draught'] = extract_value(row.get('draught'))
    row['shiptypeAIS'] = extract_value(row.get('shiptypeAIS'))# 
    #row['sog'] = extract_value(row.get('sog'))  # Speed Over Ground 
    row['cog'] = extract_value(row.get('cog'))  # Course Over Ground    
    row['heading'] = extract_value(row.get('heading'))
    row['hazard'] = extract_value(row.get('hazard'))
    row['status'] = extract_value(row.get('status'))
      # Heading
    

df = pd.DataFrame(data)

df#%%

# Filter by bounding box
min_lon, max_lon = 5.0, 6.0
min_lat, max_lat = 51.0, 52.0

geo_filtered = df[
    (df['longitude'] >= min_lon) & (df['longitude'] <= max_lon) &
    (df['latitude'] >= min_lat) & (df['latitude'] <= max_lat)
]

# Filter by specific track_id
track_id_to_select = "0fae44db86af1b4c52eb694675112290"
final_filtered = geo_filtered[geo_filtered['track_id'] == track_id_to_select]

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    final_filtered,
    geometry=[Point(xy) for xy in zip(final_filtered.longitude, final_filtered.latitude)],
    crs="EPSG:4326"
)

# Export to GeoJSON
gdf.to_file("filtered_data.geojson", driver="GeoJSON")

# Plot all unique track_id paths
plt.figure(figsize=(10, 10))
for track_id, group in geo_filtered.groupby('track_id'):
    plt.plot(group['longitude'], group['latitude'], linestyle='-', label=track_id)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Ship Tracks')
plt.grid()
#plt.legend()
plt.show()

# %%

print(gdf.columns)
# Select the track_id with the highest speed over ground
if 'sog' in gdf.columns:
    idx_max_sog = gdf['sog'].idxmax()
    track_id_max_sog = gdf.loc[idx_max_sog, 'track_id']
    gdf_highest_sog = gdf[gdf['track_id'] == track_id_max_sog]
    print(f"Track ID with highest SOG: {track_id_max_sog}")
else:
    print("Column 'SOG' not found in GeoDataFrame.")
# %%
