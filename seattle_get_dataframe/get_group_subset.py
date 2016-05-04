import pandas as pd
import numpy as np



groups = ['ASSAULTS', 'BURGLARY', 'DISTURBANCES', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT', 'TRAFFIC RELATED CALLS',
'TRESPASS']

data = pd.read_csv('~/Documents/seattle_data/911.csv')
subset_index = [(x in groups) for x in data['Event Clearance Group']]
subset = data[subset_index]
subset = subset[['Event Clearance Group', 'Event Clearance Date',
'Longitude', 'Latitude']]

subset.to_csv('~/Documents/seattle_data/911_group_subset.csv', index=False)

