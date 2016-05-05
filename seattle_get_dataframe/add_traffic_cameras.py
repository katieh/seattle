from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_private_2.csv')

## traffic cams
traffic_cams = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/traffic_cameras.csv')
traffic_cams = traffic_cams['LOCATION']

dists = [0.25, 0.5, 1, 2, 4, 8]

for dist in dists:

  traffic = []
  for i in range(data_911.shape[0]):

    if i % 10000 == 0:
      print i

    crime_loc = (data_911.iloc[i, :]['Longitude'],
                 data_911.iloc[i, :]['Latitude'])

    traffic.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
  for x in traffic_cams]))

  data_911['traffic_cameras'] = pd.Series(traffic)

  data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_traffic_' + str(dist) + '.csv', index=False)



