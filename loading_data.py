def loading_datasets(dataset):
    # open file
    df = xr.open_dataset(dataset)
    print(df) # read the datafile

    # store chlor_a dataset in variable first
    chlor_a = df.chlor_a #(can call chlor_a instead of df.chlor_a)
    return chlor_a