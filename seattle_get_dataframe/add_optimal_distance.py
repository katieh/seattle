from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_features_0.5.csv')

## parks
data_parks = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/parks.csv')

## private schools location
private_schools = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/private_schools.csv')
private_schools = private_schools['Shape']

## traffic cams
traffic_cams = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/traffic_cameras.csv')
traffic_cams = traffic_cams['LOCATION']

## fishing piers locations
fishing_piers = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/fishing_piers.csv')
fishing_piers = [(x, y) for x, y in zip(fishing_piers['LONGITUDE'], fishing_piers['LATITUDE'])]

park = []
private = []
traffic = []
fishing = []
for i in range(data_911.shape[0]):

  if i % 10000 == 0:
    print i

  crime_loc = (data_911.iloc[i, :]['Longitude'],
               data_911.iloc[i, :]['Latitude'])

  dist = 4
  park.append(sum([haversine((longi, lat), crime_loc, miles=True) <= dist
    for longi, lat in zip(data_parks['X Coord'], data_parks['Y Coord'])]))

  dist = 2
  private.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
  for x in private_schools]))

  dist = 4
  traffic.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
  for x in traffic_cams]))

  dist = 2
  fishing.append(sum([haversine((float(x[0]), float(x[1])), crime_loc, miles=True) <= dist
  for x in fishing_piers]))

data_911['park'] = pd.Series(park)
data_911['private_schools'] = pd.Series(private)
data_911['traffic_cameras'] = pd.Series(traffic)
data_911['fishing_piers'] = pd.Series(fishing)

data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_features.csv', index=False)

