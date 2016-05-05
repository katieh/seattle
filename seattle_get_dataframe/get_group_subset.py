import pandas as pd
import numpy as np
from datetime import datetime

groups = ['ASSAULTS', 'BURGLARY', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT', 'TRESPASS', 'AUTO THEFTS']

## subset the data for the appropriate groups
data = pd.read_csv('/Users/KatieHanss/Documents/seattle_data_too_big/911.csv')
subset_index = [(x in groups) for x in data['Event Clearance Group']]
data_911 = data[subset_index]
data_911 = data_911[['Event Clearance Group', 'Event Clearance Date',
'Longitude', 'Latitude']]

## subset again to make sure everything has a date and time
indicies = [not isinstance(x, float) for x in data_911['Event Clearance Date']]
data_911 = data_911.iloc[indicies, :]

## extract time features
data_911['Event Clearance Date'] = [datetime.strptime(x, '%m/%d/%Y %I:%M:%S %p') for x in data_911['Event Clearance Date']]
data_911['hour'] = [x.hour for x in data_911['Event Clearance Date']]
data_911['month'] = [x.month for x in data_911['Event Clearance Date']]
data_911['day'] = [x.day for x in data_911['Event Clearance Date']]
data_911['weekday'] = [x.weekday() for x in data_911['Event Clearance Date']]

data_911.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_subset.csv', index=False)

