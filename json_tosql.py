import pandas as pd
import sqlite3

def formatting():
    """
    Format the data from the json file and save it in a pandas DataFrame
    Parameters
    ---
    None
    
    Returns
    ---
    pd.DataFrame
        The formatted data
    """
    df = pd.read_json('data.json', )
    df.columns = df.iloc[0]
    df = df[1:]
    df.drop(df[df['t'] == 'mq'].index, inplace = True)
    df['t'] = df['t'].astype(float) - 273.15
    data = df[['numer_sta','date','ff','t','u']]
    data.loc[:,'date'] = pd.to_datetime(data['date'])
    data.columns = ['NUM_STATION', 'DATE', 'VITESSE_VENT', 'TEMPERATURE', 'HUMIDITE']
    return data

def to_sql(data):
    """
    Save the data in a sqlite database

    Parameters
    ---
    data : pd.DataFrame
        The data to save

    Returns
    ---
    None
    """

    conn = sqlite3.connect('data.db')
    data.to_sql('meteo', conn, if_exists='replace', index = False)


print(pd.read_sql('SELECT * FROM meteo', sqlite3.connect('data.db')))