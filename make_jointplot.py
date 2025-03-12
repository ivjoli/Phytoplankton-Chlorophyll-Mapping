def make_jointplot(dataframe):
    
    # Add log-transformed columns
    dataframe['Log Distance (m)'] = np.log10(dataframe['Distance to Coastline (m)']) # log of the distance
    dataframe['Log Chlorophyll (mg/m³)'] = np.log10(dataframe['Chlorophyll Concentration (mg/m³)']) # log of the chlorophyll

    # Create points for the x and y axes
    min_x = dataframe['Log Distance (m)'].min()
    max_x = dataframe['Log Distance (m)'].max()
    min_y = dataframe['Log Chlorophyll (mg/m³)'].min()
    max_y = dataframe['Log Chlorophyll (mg/m³)'].max()

    # Add some padding
    x_padding = (max_x - min_x) * 0.05
    y_padding = (max_y - min_y) * 0.05

    # Create a jointplot with log-transformed data
    chl_jointplot = sns.jointplot(
        x='Log Distance (m)', 
        y='Log Chlorophyll (mg/m³)', 
        data=dataframe,
        kind='hist',  
        xlim=(min_x - x_padding, max_x + x_padding),
        ylim=(min_y - y_padding, max_y + y_padding),
        cmap='viridis'
    )

    chl_jointplot.set_axis_labels('Log Distance to Coastline (m)', 'Log Chlorophyll Concentration (mg/m³)')
    chl_jointplot.fig.suptitle('Log Distance to Coastline vs. Log Chlorophyll Concentration (california)')
