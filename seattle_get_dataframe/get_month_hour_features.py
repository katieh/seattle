import pandas as pd
from datetime import datetime
import numpy as np

data_911 = pd.read_csv('~/Documents/seattle_data/911_w_parks.csv')

print data_911.shape
indicies = [not isinstance(x, float) for x in data_911['Event Clearance Date']]
data_911 = data_911.iloc[indicies, :]

data_911['Event Clearance Date'] = [datetime.strptime(x, '%m/%d/%Y %I:%M:%S %p') for x in data_911['Event Clearance Date']]
data_911['hour'] = [x.hour for x in data_911['Event Clearance Date']]
data_911['month'] = [x.month for x in data_911['Event Clearance Date']]
data_911['day'] = [x.day for x in data_911['Event Clearance Date']]
data_911['weekday'] = [x.weekday() for x in data_911['Event Clearance Date']]

data_911.to_csv('~/Documents/seattle_data/911_with_hour_month.csv')