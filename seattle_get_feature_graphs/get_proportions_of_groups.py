import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

labels = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_labels.csv')

groups = ['ASSAULTS', 'BURGLARY', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT',
'TRESPASS']

'''groups = ['ASSAULTS', 'BURGLARY', 'DISTURBANCES', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT', 'TRAFFIC RELATED CALLS',
'TRESPASS']'''

size = []
for label in np.unique(labels['0']):
  size.append(len(labels[labels['0'] == label]))


fig = {
    'data': [{'labels': groups,
              'values': size,
              'type': 'pie'}],
    'layout': {'title': 'Proportion of Crime Types'}
}

url = py.plot(fig, filename='Pie Chart of Crime Types')