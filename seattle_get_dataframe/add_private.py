from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_parks_4.csv')

## private schools location
private_schools = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/private_schools.csv')
private_schools = private_schools['Shape']

dists = [0.25, 0.5, 1, 2, 4, 8]

for dist in dists:

  private = []
  for i in range(data_911.shape[0]):

    if i % 10000 == 0:
      print i

    crime_loc = (data_911.iloc[i, :]['Longitude'],
                 data_911.iloc[i, :]['Latitude'])

    private.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
    for x in private_schools]))

  data_911['private_schools'] = pd.Series(private)

  data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_private_' + str(dist) + '.csv', index=False)



