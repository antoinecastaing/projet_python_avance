import pandas as pd


def get_data(date):
    """
    Get the data from the meteo france website

    Parameters
    ----------
    date : str
        The date of the data to get

    Returns
    -------
    pd.DataFrame
        The data from the website
    """
    date = pd.to_datetime(date).strftime("%Y-%m-%d")
    print(date)
    date_list = pd.date_range(start="1996-01-01", end=date, freq = "ME").strftime("%Y-%m-%d").tolist()
    df = pd.DataFrame()
    for date in date_list:
        print(date)
        date = date.replace("-", "")[:6]
        url = f"https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{date}.csv.gz"
        data = pd.read_csv(url, compression='gzip', sep=";", header=None)
        df = pd.concat([df, data])
    df.reset_index(inplace=True)
    df.columns = df.iloc[0]
    df = df[1:]
    data = df[['numer_sta','date','ff','t','u']]
    return data

def to_json(data):
    """
    Transforms a csv file into a json file

    Parameters 
    ----------
    data : pd.DataFrame
        The data to transform

    Returns
    -------
    None
    """
    with open("data.json", "w") as file:
        file.write(data.to_json())


def main():
    """
    Main function to get the data from the meteo france website and transform it into a json file
    """
    today = pd.to_datetime("today").strftime("%Y-%m-%d")
    data = get_data(today)
    to_json(data)


if __name__ == "__main__":
    main()