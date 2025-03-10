# other files in repo
from converting_units import *  # to load the data

# define function for calculating distance between two points
def calc_distance(data, coastline_data):
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
    for line in coastline_data.geoms:    # gets each line in coastline
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

    # convert degrees to meters
    # Convert distances from degrees to meters
    distances_meters = degrees_to_meters(distances, valid_points)

    return distances_meters, valid_chlorophyll, valid_points

def plot_distances(distances, chl, xlab = "", ylab = "", title = ""):
    plt.figure(figsize=(10, 6))
    plt.scatter(distances, chl, s=5, alpha=0.7, c=distances, cmap='viridis')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.show()

def log_plot(data, xlab = "", ylab="", title=""):
    calc_distance(data)
    # plot the data in log-log scale
    plt.loglog(distances, valid_chlorophyll, 'go', markersize=1)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.show()
