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
calc_distance(chlor_a) # all chloraphyll
# for california ONLY
subset = chlor_a.sel(lat=slice(50, 10), lon=slice(-180, -110))
calc_distance(subset) # chloraphyll distance in california

