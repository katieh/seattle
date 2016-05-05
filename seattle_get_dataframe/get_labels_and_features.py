import pandas as pd
from sklearn.cross_validation import StratifiedKFold


groups = ['ASSAULTS', 'BURGLARY', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT',
'TRESPASS', 'AUTO THEFTS']

## read in dataframe
features = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_parks_4.csv')

## get labels
labels = pd.DataFrame([groups.index(x) for x in features['Event Clearance Group']])

## drop non-features
features.drop('Event Clearance Group', axis = 1, inplace=True)
features.drop('Event Clearance Date', axis=1, inplace=True)
features.drop('day', axis = 1, inplace=True)
features.drop('weekday', axis = 1, inplace=True)
features.drop('month', axis = 1, inplace=True)
features.drop('hour', axis = 1, inplace=True)


## half the data we use, the other half we save for later
skf = list(StratifiedKFold(labels[0], n_folds=2))

hold_out_indecies, train_indecies = skf[0]

hold_out_x = features.iloc[hold_out_indecies, :]
hold_out_y =  labels.iloc[hold_out_indecies]

train_x = features.iloc[train_indecies, :]
train_y = labels.iloc[train_indecies]

train_y.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_labels.csv', index=False)
train_x.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_features.csv', index=False)

hold_out_y.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_labels_hold_out.csv', index=False)
hold_out_x.to_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_features_hold_out.csv', index=False)
