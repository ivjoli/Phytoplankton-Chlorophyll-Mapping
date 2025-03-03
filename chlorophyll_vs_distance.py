# add this to import the necessary libraries
import geopandas as gpd
from shapely.geometry import Point, MultiLineString
from scipy.spatial import cKDTree
from cartopy.io import shapereader as shpreader
from shapely.ops import unary_union

# define function for calculating distance between two points
def calc_distance(data):
    # load the coastline data
    shp_path = shpreader.natural_earth(resolution='110m', category='physical', name='coastline') # load the natural earth data from physical coatsline at reso 110 for fast work
    coastline_shapes = list(shpreader.Reader(shp_path).geometries()) # read the data as geometries and put it as a list
    coastline = unary_union(MultiLineString(coastline_shapes)) # combine the geometries into one multilinestring

    # get the lat/lon and filtuer out NAN chlorophyll values
    lats, lon = data['lat'].values, data['lon'].values # put the values of lat and lon in variables
    lon_grid, lat_grid = np.meshgrid(lon, lats) # create a meshgrid of the lat and lon

    # create valid points (points without NAN chlo values)
    valid_points = [] # list to store all valid points
    for lon, lat, chl in zip(lon_grid.flatten(), lat_grid.flatten(), data.values.flatten()):
        if not np.isnan(chl): # if the chl value is not NAN
            point = Point(lon, lat) # create a point using lon and lat
            valid_points.append(point) # add point to the list

    valid_chlorophyll = [] # list to store all valid chl values
    for chl in data.values.flatten():
        if not np.isnan(chl): # if the chl value is not NAN
            valid_chlorophyll.append(chl) # add chl value to the list
        
    # extract coordinates from multilinestring
    coastline_coords_list = []  # a list of coordinates
    for line in coastline.geoms:    # gets each line in coastline
        for coord in line.coords:   # gets each coordinate in line  
            coastline_coords_list.append(coord)     # adds the coordinate to the list
    coastline_coords = np.array(coastline_coords_list) # converts the list to an array
        
    # create a KDTree for coastline coordinates
    tree = cKDTree(coastline_coords)

    # find the closest coastline point for each valid point
    distances = [] # list to store all distances
    for point in valid_points: # for each point in the list of valid points
        dist, idx = tree.query([point.x, point.y]) # find the distance and index of the closest point in the coastline
        distances.append(dist) # add the distance to the list

    plt.figure(figsize=(10, 6))
    plt.scatter(distances, valid_chlorophyll, s=5, alpha=0.7, c=distances, cmap='viridis')
    plt.xlabel("Distance to Coastline (degrees)")
    plt.ylabel("Chlorophyll Concentration")
    plt.title("Distance to Coastline vs Chlorophyll Concentration")
    plt.show()

def log(distances, valid_chlorophyll):
    # plot the data in log-log scale
    plt.loglog(distances, valid_chlorophyll, 'go', markersize=1)