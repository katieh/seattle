from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_traffic_4.csv')

## fishing piers locations
fishing_piers = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/fishing_piers.csv')
fishing_piers = [(x, y) for x, y in zip(fishing_piers['LONGITUDE'], fishing_piers['LATITUDE'])]

dists = [0.25, 0.5, 1, 2, 4, 8]

for dist in dists:

  fishing = []
  for i in range(data_911.shape[0]):

    if i % 10000 == 0:
      print i

    crime_loc = (data_911.iloc[i, :]['Longitude'],
                 data_911.iloc[i, :]['Latitude'])

    fishing.append(sum([haversine((float(x[0]), float(x[1])), crime_loc, miles=True) <= dist
  for x in fishing_piers]))

  data_911['fishing_piers'] = pd.Series(fishing)

  data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_fishing_' + str(dist) + '.csv', index=False)



