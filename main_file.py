# import the libraries
# other files in repo
from loading_data import *  # to load the data
from simple_plots import *  # to plot simple data
from chlorophyll_vs_distance import *  # to calculate distance
from make_jointplot import *  # to make the jointplot

import xarray as xr # for reading and loading dataset

# general number libraries
import pandas as pd
import numpy as np

# for mapping
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import geopandas as gpd

# calculating distances
from shapely.geometry import Point, MultiLineString
from scipy.spatial import cKDTree
from cartopy.io import shapereader as shpreader
from shapely.ops import unary_union

# using seaborn
import seaborn as sns


print("please enter the datafile") 
dataset = input()
if dataset == "q": # exit the program
    quit()

# load the dataset
chlor_a = loading_datasets(dataset) 
coastline = loading_coastline()


# plotting the data
plot_chlor_a(chlor_a)
# plot the data but in california ONLY
plot_chlor_a_CA(chlor_a)
# more colors
adding_colors(chlor_a)

# caculate the distance
# for california ONLY
subset = chlor_a.sel(lat=slice(50, 10), lon=slice(-180, -110))
distances_CA, valid_chlorophyll_CA, valid_points_CA = calc_distance(subset, coastline) # chloraphyll distance in california
################################################################
distances, valid_chlorophyll, valid_points = calc_distance(chlor_a, coastline) # all chloraphyll

# plot distances
plot_distances(distances, valid_chlorophyll, "Distance to Coastline (meters)", "Chlorophyll Concentration (mg/m^3)", "Distance to Coastline vs Chlorophyll Concentration, MODIS Jan 2023")


# get the log of the data
# get the log of the data
log_plot(subset, coastline. "Distance to coastline", "Chlorophyll Concentration (mg/m^3)", "Distance to Coastline for California (Log)" ) # log of the data in california
log_plot(chlor_a, coastline, "Distance to coastline", "Chlorophyll Concentration (mg/m^3)", "Distance to Coastline (Log)") # log of all the data

#--------------------------------------
# using seaborn
# create a new panda dataframe with the distance
distance_df = pd.DataFrame({
    'Distance to Coastline (m)': distances > 0, # ensure the distance is greater than 0 for log
    'Chlorophyll Concentration (mg/m³)': valid_chlorophyll > 0 # ensure the chlorophyll is greater than 0 for log
}) 

# create a jointplot of distance vs chlorophyll concentration
make_jointplot(distance_df)