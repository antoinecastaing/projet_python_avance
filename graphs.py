import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3

def get_data():
    """
    Get the data from the sqlite database

    Parameters
    ---
    None

    Returns
    ---
    pd.DataFrame
        The data from the database
    """
    conn = sqlite3.connect('data.db')
    data = pd.read_sql_query("SELECT * FROM meteo", conn)
    return data

def plot(data, station_number):
    """
    Plot the data in graphs and save them in the graphs folder

    Parameters
    ---
    data : pd.DataFrame
        The data to plot
    station_number : string
        The id of the station to plot
    Returns
    ---
    None
    """
    sns.lineplot(data = data[data["NUM_STATION"] == station_number], x = data["ANNEE"], y = data["TEMPERATURE"])
    plt.savefig(f"graphs/temperature_{station_number}.png")

def main():
    """
    Main function to get the data and plot it
    """
    data = get_data()
    plot(data, "07005")

if __name__ == "__main__":
    main()