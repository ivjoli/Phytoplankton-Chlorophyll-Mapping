# used for tracking units
from unyt.unit_symbols import degree, m
def degrees_to_meters(distances, points):
    """Convert distances from degrees to meters at specified geographic points."""
    distance_in_meters = [] # list to store all distances in meters

    for dist, point in zip(distances, points):
        #Earth's radius in meters
        earth_radius = 6371000
        # 1 degree = 2pi*radius/360 meters at equater
        meters_per_degree = (2*np.pi*earth_radius) / 360
        
        # convert lat 
        lat_distance = dist*meters_per_degree # convert to meters
        
        # convert lon
        latitude_rad = point.y * (np.pi / 180) # lat -> radians for scaling
        lon_distance = dist * meters_per_degree * np.cos(latitude_rad)

        # pythagorean theorem for total distance in meters
        total_distance = np.sqrt(lat_distance**2 + lon_distance**2)
        distance_in_meters.append(total_distance) # add the point into the list

    return distance_in_meters # return the list