# import the libraries
# other files in repo
from loading_data import *
from simple_plots import *

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


