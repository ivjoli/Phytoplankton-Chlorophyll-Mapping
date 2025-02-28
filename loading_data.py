import xarray as xr # for reading and loading dataset

# general number libraries
import pandas as pd
import numpy as np

# for mapping
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# calculating distance
import geopandas as gpd
from shapely.geometry import Point, MultiLineString
from scipy.spatial import cKDTree

 # open file
df = xr.open_dataset("")
print(df) # read the datafile

# store chlor_a dataset in variable first
chlor_a = df.chlor_a #(can call chlor_a instead of df.chlor_a)