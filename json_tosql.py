import pandas as pd
import sqlite3
df = pd.read_json('data.json', )
df.columns = df.iloc[0]
df = df[1:]
df.drop(df[df['t'] == 'mq'].index, inplace = True)
df['t'] = df['t'].astype(float) - 273.15
data = df[['numer_sta','date','ff','t','u']]
data.loc[:,'date'] = pd.to_datetime(data['date'])
data.columns = ['NUM_STATION', 'DATE', 'VITESSE_VENT', 'TEMPERATURE', 'HUMIDITE']

data.to_sql('meteo', sqlite3.connect('data.db'), if_exists='replace', index=False)

print(pd.read_sql('SELECT * FROM meteo', sqlite3.connect('data.db')))