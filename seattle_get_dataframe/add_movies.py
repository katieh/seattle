from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_traffic_4.csv')

## fishing piers locations
movie_theaters = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/movie_theaters.csv')
movie_theaters = [x.replace('(', '').replace(')', '') for x in movie_theaters['Shape']]

dists = [0.25, 0.5, 1, 2, 4, 8]

for dist in dists:

  movie = []
  for i in range(data_911.shape[0]):

    if i % 10000 == 0:
      print i

    crime_loc = (data_911.iloc[i, :]['Longitude'],
                 data_911.iloc[i, :]['Latitude'])

    movie.append(sum([haversine((float(x.split(', ')[1]), float(x.split(', ')[0])), crime_loc, miles=True) <= dist
  for x in movie_theaters]))

  data_911['movie_theaters'] = pd.Series(movie)

  data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_movies_' + str(dist) + '.csv', index=False)



