import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np
import contextily as ctx

# Load your data
df = pd.read_csv('all_flickr_post.csv')

# Generate KDE
x = df['longitude']
y = df['latitude']
xy = np.vstack([x,y])
z = gaussian_kde(xy)(xy)

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))
gdf.crs = "EPSG:4326"  # WGS 84, common lat/lon CRS

# Generate plot
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
gdf.plot(column=z, ax=ax, legend=True, cmap='viridis', markersize=10)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.Stamen.TonerLite)
plt.title('Density of Flickr Posts in Parks')
plt.show()



