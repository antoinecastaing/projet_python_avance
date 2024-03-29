import pandas as pd

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
    df = pd.read_json('data.json')
    print(df.head())
    df.drop(df[df['t'] == 'mq'].index, inplace = True)
    df.drop(df[df['t']=='t'].index, inplace = True)
    df['t'] = df['t'].astype(float) - 273.15
    data = df[['numer_sta','date','ff','t','u']]
    data.loc[:,'date'] = pd.to_datetime(data['date'])
    data.columns = ['NUM_STATION', 'DATE', 'VITESSE_VENT', 'TEMPERATURE', 'HUMIDITE']
    data["ANNEE"] = pd.DatetimeIndex(data["DATE"]).year
    data["MOIS"] = pd.DatetimeIndex(data["DATE"]).month
    data["JOUR"] = pd.DatetimeIndex(data["DATE"]).day
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

    data.to_sql('meteo', 'sqlite:///data.db', if_exists='replace')


def main():
    """
    Main function to format the data and save it in a sqlite database
    """
    data = formatting()
    to_sql(data)

if __name__ == "__main__":
    main()