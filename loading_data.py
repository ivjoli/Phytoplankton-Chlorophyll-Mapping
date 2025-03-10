def loading_datasets(dataset):
    # open file
    df = xr.open_dataset(dataset)
    
    # store chlor_a dataset in variable first
    chlor_a = df.chlor_a #(can call chlor_a instead of df.chlor_a)
    return chlor_a

def loading_coastline():
    #Load coastline data
    shp_path = shpreader.natural_earth(resolution="110m", category="physical", name="coastline")
    coastline_shapes = list(shpreader.Reader(shp_path).geometries())
    coastline = unary_union(MultiLineString(coastline_shapes))  # Combine into a single MultiLineString
    return coastline