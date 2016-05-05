from haversine import haversine
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/auto_thefts.csv')
parks = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/parks.csv')

## seattle police precincts
spd_precints = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/SPD_precinct.csv')

precincts = []
for row in spd_precints.iterrows():
  precincts = precincts + row[1]['the_geom'].replace('(', '').replace(')', '').replace('MULTIPOLYGON ', '').split(', ')

## public bathrooms
bathrooms = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/bathrooms.csv')
bathrooms = [x.replace('POINT (', '').replace(')', '') for x in bathrooms['the_geom']]

## parking
parking = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/parking.csv')
parking = parking['SHAPE']

## traffic cams
traffic_cams = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/traffic_cameras.csv')
traffic_cams = traffic_cams['LOCATION']

## private schools location
private_schools = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/private_schools.csv')
private_schools = private_schools['Shape']

## public schools location
public_schools = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/public_schools.csv')
public_schools = public_schools['Shape']

## baseball field locations
baseball_fields = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/baseball_fields.csv')
baseball_fields = [x.replace('POINT (', '').replace(')', '') for x in baseball_fields['the_geom']]

## basketball court locations
basketball_courts = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/basketball_courts.csv')
bball = []
for row in basketball_courts.iterrows():
  bball.append(row[1]['the_geom'].replace('(', '').replace(')', '').replace('MULTIPOLYGON ', '').split(', ')[0])

## fishing piers locations
fishing_piers = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/fishing_piers.csv')
fishing_piers = [(x, y) for x, y in zip(fishing_piers['LONGITUDE'], fishing_piers['LATITUDE'])]

## golf courses
golf_courses = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/golf_course.csv')
golf_courses = [x.replace('POINT (', '').replace(')', '') for x in golf_courses['the_geom']]

## movie theaters
movie_theaters = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/movie_theaters.csv')
movie_theaters = [x.replace('(', '').replace(')', '') for x in movie_theaters['Shape']]

## skate parks
skate_parks = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/skate_park.csv')
skate_parks = [(x, y) for x, y in zip(skate_parks['LONGITUDE'], skate_parks['LATITUDE'])]

## tracks
tracks = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/tracks.csv')
tracks = [x.replace('POINT (', '').replace(')', '') for x in tracks['the_geom']]

## trails
trails = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/trails.csv')
trails = [x.replace('LINESTRING (', '').replace(')', '').split(', ') for x in trails['the_geom']]

park = []
spd = []
restrooms = []
garages = []
traffic = []
private = []
public = []
baseball = []
basketball = []
fishing = []
golf = []
movie = []
skate = []
track = []
trail = []

dist = 0.5

for i in range(data_911.shape[0]):

  print i

  crime_loc = (data_911.iloc[i, :]['Longitude'],
             data_911.iloc[i, :]['Latitude'])

  park.append(sum([haversine((longi, lat), crime_loc, miles=True) <= dist
  for longi, lat in zip(parks['X Coord'], parks['Y Coord'])]))

  spd.append(int(any([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
  for x in precincts])))

  restrooms.append(sum([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
  for x in bathrooms]))

  garages.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
  for x in parking]))

  traffic.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
  for x in traffic_cams]))

  private.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
  for x in private_schools]))

  public.append(sum([haversine((float(x.split(', ')[1].replace(')', '')), float(x.split(', ')[0].replace('(', ''))), crime_loc, miles=True) <= dist
  for x in public_schools]))

  baseball.append(sum([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
  for x in baseball_fields]))

  basketball.append(sum([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
  for x in bball]))

  fishing.append(sum([haversine((float(x[0]), float(x[1])), crime_loc, miles=True) <= dist
  for x in fishing_piers]))

  golf.append(sum([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
  for x in golf_courses]))

  movie.append(sum([haversine((float(x.split(', ')[1]), float(x.split(', ')[0])), crime_loc, miles=True) <= dist
  for x in movie_theaters]))

  skate.append(sum([haversine((float(x[0]), float(x[1])), crime_loc, miles=True) <= dist
  for x in skate_parks]))

  track.append(sum([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
  for x in tracks]))

  trail.append(sum([int(any([haversine((float(x.split(' ')[0]), float(x.split(' ')[1])), crime_loc, miles=True) <= dist
  for x in t])) for t in trails]))

data_911['parks'] = pd.Series(park)
data_911['spd'] = pd.Series(spd)
data_911['restrooms'] = pd.Series(restrooms)
data_911['garages'] = pd.Series(garages)
data_911['traffic_cameras'] = pd.Series(traffic)
data_911['private_schools'] = pd.Series(private)
data_911['public_schools'] = pd.Series(public)
data_911['baseball_fields'] = pd.Series(baseball)
data_911['basketball_courts'] = pd.Series(basketball)
data_911['fishing_piers'] = pd.Series(fishing)
data_911['golf_courses'] = pd.Series(golf)
data_911['movie_theaters'] = pd.Series(movie)
data_911['skate_parks'] = pd.Series(skate)
data_911['track_and_fields'] = pd.Series(track)
data_911['trails'] = pd.Series(trail)

data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/auto_theft_w_features.csv', index=False)