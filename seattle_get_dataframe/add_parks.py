from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_subset.csv')
data_parks = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/parks.csv')

dist = 16

park = []
for i in range(data_911.shape[0]):

  if i % 10000 == 0:
    print i

  crime_loc = (data_911.iloc[i, :]['Longitude'],
               data_911.iloc[i, :]['Latitude'])

  park.append(sum([haversine((longi, lat), crime_loc, miles=True) <= dist
    for longi, lat in zip(data_parks['X Coord'], data_parks['Y Coord'])]))

data_911['park'] = pd.Series(park)

data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_parks.csv', index=False)



