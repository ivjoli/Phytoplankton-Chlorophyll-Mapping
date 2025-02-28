## plotting the entire month of janurary
chlor_a.plot()


## plotting the chlorophyll in just california
# lat = (20, 40)
# lon = (-150, -100)

#copy the plot
chlor_copy = chlor_a.copy()

# # plotting it
CA_chl = chlor_copy.sel(lat=slice(50, 10), lon=slice(-180, -110)) # slices until the lon and lat coordinates
CA_chl = CA_chl.where(~np.isnan(CA_chl))  # filters out the NAN values
#print(subset)
CA_chl.plot()


# adding more coloring
chlor_a.plot(cmap='viridis', robust=True)