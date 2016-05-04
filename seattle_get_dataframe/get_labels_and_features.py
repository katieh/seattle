import pandas as pd

groups = ['ASSAULTS', 'BURGLARY', 'DISTURBANCES', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT', 'TRAFFIC RELATED CALLS',
'TRESPASS']

features = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_with_hour_month.csv')

labels = pd.DataFrame([groups.index(x) for x in features['Event Clearance Group']])
features.drop('Event Clearance Group', axis = 1, inplace=True)
features.drop('Event Clearance Date', axis=1, inplace=True)

labels.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_labels.csv', index=False)
features.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_features.csv', index=False)
