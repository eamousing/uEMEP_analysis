import pandas as pd
import glob

col_names = ["Parameter", "Site", "SiteID", "Latitude", "Longitude", "Conc", "Unit", 
             "DateTime_start", "DateTime_end", "CCode", "Category"]

def read_observations_airnow(dir, col_names=col_names):
    """
    Read and concatenate multiple CSV files containing air quality observations.

    Parameters:
    dir (str): The directory path where the CSV files are located.
    col_names (list): A list of column names for the resulting dataframe.

    Returns:
    pandas.DataFrame: A dataframe containing the concatenated data from all CSV files.
    """

    # Get list of all csv files in the directory
    files = glob.glob(dir + "/*.csv")

    # Initialize an empty list to hold the dataframes
    dataframes = []

    # Read and append files to dataframe
    for file in files:
        df = pd.read_csv(file, names=col_names)
        dataframes.append(df)
    
    # Concatenate all dataframe
    all_data = pd.concat(dataframes, ignore_index=True)

    return all_data
