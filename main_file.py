# import the libraries
# other files in repo
from loading_data import *  # to load the data
from simple_plots import *  # to plot simple data
from chlorophyll_vs_distance import *  # to calculate distance

import xarray as xr # for reading and loading dataset

# general number libraries
import pandas as pd
import numpy as np

# for mapping
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

print("please enter the datafile") 
dataset = input()
if dataset == "q": # exit the program
    quit()

# load the dataset
chlor_a = loading_datasets(dataset)


# plotting the data
plot_chlor_a(chlor_a)
# plot the data but in california ONLY
plot_chlor_a_CA(chlor_a)
# more colors
adding_colors(chlor_a)

# caculate the distance
# for california ONLY
subset = chlor_a.sel(lat=slice(50, 10), lon=slice(-180, -110))
distances_CA, valid_chlorophyll_CA = calc_distance(subset) # chloraphyll distance in california
################################################################
distances, valid_chlorophyll = calc_distance(chlor_a) # all chloraphyll

# plot distances
plot_distances(distances, valid_chlorophyll, "Distance to Coastline (degrees)", "Chlorophyll Concentration", "Distance to Coastline vs Chlorophyll Concentration, MODIS Jan 2023")


# get the log of the data
log(subset) # log of the data in california
log(chlor_a) # log of all the data