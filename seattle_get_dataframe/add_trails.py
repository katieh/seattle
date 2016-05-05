from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_traffic_4.csv')

## trails
trails = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/trails.csv')
trails = [x.replace('LINESTRING (', '').replace(')', '').split(', ') for x in trails['the_geom']]

dists = [0.25, 0.5, 1, 2, 4, 8]

for dist in dists:

  movie = []
  for i in range(data_911.shape[0]):

    if i % 10000 == 0:
      print i

    crime_loc = (data_911.iloc[i, :]['Longitude'],
                 data_911.iloc[i, :]['Latitude'])

    trail.append(sum([int(any([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
    for x in t])) for t in trails]))

  data_911['trails'] = pd.Series(trail)

  data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_trails_' + str(dist) + '.csv', index=False)



